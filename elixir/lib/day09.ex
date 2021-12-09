
defmodule Aoc2021.Day09 do
  alias Aoc2021.Parse

  def index(arr, {x, y}) do
    if y >= 0 and y < tuple_size(arr) do
      line = elem(arr, y)
      if x >= 0 and x < tuple_size(line) do
        [elem(line, x)]
      else
        []
      end
    else
      []
    end
  end

  def coordinates({x, y}) do
    [{x-1, y}, {x+1, y}, {x, y-1}, {x, y+1}]
  end

  def around(arr, {x, y}) do
    coordinates({x, y})
    |> Enum.map(&index(arr, &1))
    |> Enum.concat()
  end

  def zip_around(arr, {x, y}) do
    coordinates({x, y})
    |> Enum.map(&index(arr, &1))
    |> Enum.zip(coordinates({x, y}))
    |> Enum.filter_map(fn {a, _} -> length(a) != 0 end, fn {[a], b} -> {a, b} end)
    |> Enum.to_list()
    |> List.flatten()
  end

  def find_lowest(arr) do
    (for y <- 0..(tuple_size(arr)-1),
        x <- 0..(tuple_size(elem(arr, 0))-1),
        Enum.all?(around(arr, {x, y}), &(hd(index(arr, {x, y})) < &1)),
        do: 1 + hd(index(arr, {x, y}))
     )
    |> Enum.sum()
  end

  def find_basins(arr) do
    for y <- 0..(tuple_size(arr)-1),
        x <- 0..(tuple_size(elem(arr, 0))-1),
        Enum.all?(around(arr, {x, y}), &(hd(index(arr, {x, y})) < &1)),
        into: %{},
        do: {{x, y}, {x, y}}
  end

  def input(file) do
    file
    |> Parse.parse_string_lines()
    |> Enum.map(&String.split(&1, "", trim: true))
    |> Enum.map(fn line -> Enum.map(line, &String.to_integer/1) end)
    |> Enum.map(fn line -> List.to_tuple(Enum.to_list(line)) end)
    |> Enum.to_list()
    |> List.to_tuple()
  end

  def fill_basins(map, arr) do
    Map.merge(map,
      (for y <- 0..(tuple_size(arr)-1),
        x <- 0..(tuple_size(elem(arr, 0))-1),
        hd(index(arr, {x, y})) != 9,
        {h, {lx, ly}} <- zip_around(arr, {x, y}),
        Map.has_key?(map, {lx, ly}) and h < hd(index(arr, {x, y})),
        into: %{},
        do: {{x, y}, Map.get(map, {lx, ly})}
        )
    )
  end

  def distinct_values(map) do
    values = Map.values(map)
    |> Enum.uniq()

    for v <- values do
        Map.values(map)
        |> Enum.filter(&(&1 == v))
        |> Enum.count
    end
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day9/input.txt") do
    file
    |> input()
    |> find_lowest()
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day9/input.txt") do
    arr = file
    |> input()

    arr
    |> find_basins()
    |> (&Enum.reduce(0..8, &1, fn val, acc -> fill_basins(acc, arr) end)).()
    |> distinct_values()
    |> Enum.sort()
    |> Enum.reverse()
    |> Enum.take(3)
    |> Enum.product()
  end
end
