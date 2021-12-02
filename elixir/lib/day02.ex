

defmodule Aoc2021.Day02 do
  alias Aoc2021.Parse

  defp reduce1({"forward", d}, {depth, pos}), do: {depth, pos + d}
  defp reduce1({"down", d}, {depth, pos}), do: {depth + d, pos}
  defp reduce1({"up", d}, {depth, pos}), do: {depth - d, pos}

  defp reduce2({"forward", d}, {depth, pos, aim}), do: {depth + aim * d, pos + d, aim}
  defp reduce2({"down", d}, {depth, pos, aim}), do: {depth, pos, aim + d}
  defp reduce2({"up", d}, {depth, pos, aim}), do: {depth, pos, aim - d}

  defp split_string(s) do
    [l, r] = String.split(s, " ", trim: true)
    {l, String.to_integer(r)}
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day2/input.txt") do
    Parse.parse_string_lines(file)
    |> Enum.map(&split_string/1)
    |> Enum.reduce({0, 0}, &reduce1/2)
    |> Tuple.product
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day2/input.txt") do
    Parse.parse_string_lines(file)
    |> Enum.map(&split_string/1)
    |> Enum.reduce({0, 0, 0}, &reduce2/2)
    |> Tuple.product
  end
end
