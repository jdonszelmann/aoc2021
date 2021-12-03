

defmodule Aoc2021.Day03 do
  alias Aoc2021.Parse

  @spec nth_bit([binary], non_neg_integer) :: non_neg_integer
  def nth_bit(number, index), do: String.to_integer(String.at(number, index))

  @spec common([binary], non_neg_integer, :most | :least) :: non_neg_integer
  def common(lst, index, which) do
    ones = lst
    |> Enum.map(&nth_bit(&1, index))
    |> Enum.sum

    zeros = length(lst) - ones

    if which == :most do
      if(ones >= zeros, do: 1, else: 0)
    else
      if(zeros > ones, do: 1, else: 0)
    end
  end


  def for_all_bits(lst, which) do
    Enum.reduce(0..((String.length (hd lst)) - 1), "", fn x, acc -> acc <> Integer.to_string(common(lst, x, which)) end)
    |> Integer.parse(2)
    |> elem 0
  end

  def ox_or_fuel(lst, which, index \\ 0) do
    if length(lst) == 1 do
      hd(lst)
      |> to_string
      |> Integer.parse(2)
      |> elem 0
    else
      c = common(lst, index, which)

      lst
      |> Enum.filter(fn x -> nth_bit(x, index) == c end)
      |> ox_or_fuel(which, index + 1)
    end
  end


  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day3/input.txt") do
    lst = file
    |> Parse.parse_string_lines

    for_all_bits(lst, :most) * for_all_bits(lst, :least)
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day3/input.txt") do
    lst = file
    |> Parse.parse_string_lines

    ox_or_fuel(lst, :most) * ox_or_fuel(lst, :least)
  end
end
