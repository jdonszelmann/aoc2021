
defmodule Aoc2021.Day10 do
  alias Aoc2021.Parse

  def opening(?(), do: true
  def opening(?[), do: true
  def opening(?{), do: true
  def opening(?<), do: true
  def opening(_), do: false

  def closing(a), do: not opening(a)

  def closing_to_opening(?)), do: ?(
  def closing_to_opening(?]), do: ?[
  def closing_to_opening(?}), do: ?{
  def closing_to_opening(?>), do: ?<

  def autocorrect_costs(?)), do: 3
  def autocorrect_costs(?]), do: 57
  def autocorrect_costs(?}), do: 1197
  def autocorrect_costs(?>), do: 25137

  def autocomplete_costs(?(), do: 1
  def autocomplete_costs(?[), do: 2
  def autocomplete_costs(?{), do: 3
  def autocomplete_costs(?<), do: 4


  def complete(line) do
    complete(line, [])
  end

  def complete([], s), do: {0, s}
  def complete([c | rest], s) do
    cond do
      opening(c) -> complete(rest, [c | s])
      closing_to_opening(c) == hd(s) ->  complete(rest, tl s)
      true -> {autocorrect_costs(c), []}
    end
  end

  def mean(lst) do
    lst
    |> Enum.sort()
    |> Enum.drop(floor(Enum.count(lst) / 2))
    |> Enum.take(1)
    |> hd()
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day10/test.txt") do
    file
    |> Parse.parse_string_lines()
    |> Enum.map(&String.to_charlist/1)
    |> Enum.map(&complete/1)
    |> Enum.map(fn {a, b} -> a end)
    |> Enum.sum()
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day10/input.txt") do
    file
    |> Parse.parse_string_lines()
    |> Enum.map(&String.to_charlist/1)
    |> Enum.map(&complete/1)
    |> Enum.filter(fn {a, b} -> a == 0 end)
    |> Enum.map(fn {a, b} -> b end)
    |> Enum.map(fn i -> Enum.reduce(i, 0, &(&2 * 5 + autocomplete_costs(&1))) end)
    |> mean
  end
end
