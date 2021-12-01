

defmodule Day01 do
  @spec part1([non_neg_integer]) :: non_neg_integer
  defp count_increasing(ints) do
    length for {a, b} <- Stream.zip(ints, tl ints), a < b, do: 1
  end


  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day1/input.txt") do
    Parse.parse_int_lines(file)
    |> count_increasing
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day1/input.txt") do
    Parse.parse_int_lines(file)
    |> Enum.chunk_every(3, 1)
    |> Enum.map(&Enum.sum/1)
    |> Enum.to_list
    |> count_increasing
  end
end
