
defmodule Aoc2021.Day06 do
  alias Aoc2021.Parse

  def split_to_integers(line) do
    line
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
    |> Enum.to_list()
  end

  def collect(l) do
    a = Enum.frequencies(l)
    Enum.map(0..8, &Map.get(a, &1, 0))
  end

  def iterate(l) do
    [a, b, c, d, e, f, g, h, i] = l
    [b, c, d, e, f, g, h + a, i, a]
  end

  def solution(file, n) do
    file
    |> Parse.parse_string_lines()
    |> hd
    |> split_to_integers
    |> collect
    |> (&Enum.reduce(1..n, &1, fn _, acc -> iterate(acc) end)).()
    |> Enum.sum
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day6/input.txt") do
    solution(file, 80)
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day6/input.txt") do
    solution(file, 256)
  end
end