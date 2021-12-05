

defmodule Aoc2021.Day05 do
  alias Aoc2021.Parse

  def split_to_integers(line) do
    line
    |> String.split(" -> ")
    |> Enum.map(&String.split(&1, ","))
    |> Enum.to_list()
    |> List.flatten()
    |> Enum.map(&String.to_integer/1)
    |> Enum.to_list()
    |> List.to_tuple()
  end

  def sign(0), do: 0
  def sign(n), do: if(n > 0, do: 1, else: -1)

  def insert_point(m, p) do
    Map.put(m, p, Map.get(m, p, 0) + 1)
  end

  def plot_coords(_, m \\ %{})
  def plot_coords([], m), do: m
  def plot_coords([{x1, y1, x2, y2} | rest], m) do
    points = max(abs(y2 - y1), abs(x2 - x1))
    dx = sign(x2 - x1)
    dy = sign(y2 - y1)

    m = Enum.reduce(0..points, m, fn i, m -> insert_point(m, {x1 + i * dx, y1 + i * dy}) end)
    plot_coords(rest, m)
  end

  def count_doubles(m) do
    Map.values(m)
    |> Enum.filter(&(&1 > 1))
    |> Enum.count()
  end

  def solution(file, f \\ fn _ -> true end) do
    file
    |> Parse.parse_string_lines()
    |> Enum.map(&split_to_integers/1)
    |> Enum.filter(f)
    |> plot_coords()
    |> count_doubles()
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day5/input.txt") do
    solution(file, fn {x1, y1, x2, y2} -> x1 == x2 or y1 == y2 end)
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day5/input.txt") do
    solution(file)
  end
end
