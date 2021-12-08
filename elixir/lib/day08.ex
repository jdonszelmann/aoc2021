
defmodule Aoc2021.Day08 do
  alias Aoc2021.Parse

  def lengths(2), do: 1
  def lengths(3), do: 7
  def lengths(4), do: 4
  def lengths(7), do: 8

  def initial_map(input) do
    for i <- input, String.length(i) in [2, 3, 4, 7], into: %{}, do: {lengths(String.length(i)), i}
  end

  def find_pattern(i, im) do
    if Enum.all?(for c <- String.codepoints(Map.get(im, 1)), do: String.contains?(i, c)) do
      if String.length(i) == 5 do
        {3, i}
      else
        if Enum.all?(for c <- String.codepoints(Map.get(im, 4)), do: String.contains?(i, c)) do
          {9, i}
        else
          {0, i}
        end
      end
    else
      if Enum.all?(
           for c <- String.codepoints(Map.get(im, 4)),
           !String.contains?(Map.get(im, 1), c),
           do: String.contains?(i, c)
      ) and String.length(i) == 5  do
        {5, i}
      else
        if String.length(i) == 5 do
          {2, i}
        else
          {6, i}
        end
      end
    end
  end

  def build_map(input) do
    im = initial_map(input)

    input
    |> Enum.filter(fn i -> !(i in Map.values(im)) end)
    |> Enum.map(&find_pattern(&1, im))
    |> Map.new
    |> Map.merge(im)
  end

  def same_chars(a, b) do
    String.length(a) == String.length(b) and
    Enum.all?(for c <- String.codepoints(b), do: String.contains?(a, c))
  end

  def find_same_chars(number, map) do
    hd (for {k, v} <- map, same_chars(number, v), do: k)
  end

  def translate({numbers, map}) do
    numbers
    |> Enum.map(&find_same_chars(&1, map))
    |> Enum.reduce(&(&1 + 10 * &2))
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day8/input.txt") do
    file
    |> Parse.parse_string_lines()
    |> Enum.map(&String.split(&1, " | "))
    |> Enum.map(fn [_, a] -> a end)
    |> Enum.map(&String.split(&1, " ", trim: true))
    |> Enum.to_list()
    |> List.flatten()
    |> Enum.filter(fn i -> String.length(i) in [2, 3, 4, 7] end)
    |> Enum.count()
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day8/input.txt") do
    {ins, outs} =  file
    |> Parse.parse_string_lines()
    |> Enum.map(&String.split(&1, " | "))
    |> Enum.map(fn [a, b] -> {a, b} end)
    |> Enum.unzip()

    map = ins
    |> Enum.map(&String.split(&1, " ", trim: true))
    |> Enum.map(&build_map/1)

    outs
    |> Enum.map(&String.split(&1, " ", trim: true))
    |> Enum.zip(map)
    |> Enum.map(&translate/1)
    |> Enum.sum()

  end
end
