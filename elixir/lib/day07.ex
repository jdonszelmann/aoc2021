
defmodule Aoc2021.Day07 do
  alias Aoc2021.Parse

  def calculate(i, inp, f) do
    inp
    |> Enum.map(fn p -> f.(abs(p - i)) end)
    |> Enum.sum()
  end

  def solution(file, f) do
    inp = file
    |> Parse.parse_string_lines()
    |> hd
    |> Parse.split_to_integers()

    Enum.min_by(0..Enum.max(inp) * 2, &calculate(&1, inp, f))
    |> calculate(inp, f)
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day7/input.txt") do
    solution(file, fn x -> x end)
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day7/input.txt") do
    solution(file, fn x -> floor((x * (x + 1)) / 2) end)
  end
end
