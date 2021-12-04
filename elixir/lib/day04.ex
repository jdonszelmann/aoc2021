

defmodule Aoc2021.Day04 do
  alias Aoc2021.Parse

  def parse_single_board(board) do
    board
    |> Enum.map(&String.split/1)
    |> Enum.map(fn x -> Enum.map(x, &String.to_integer/1) end)
  end

  def parse_bingo_boards([inp | lines]) do
    boards = lines
    |> Enum.chunk_every(5)
    |> Enum.map(&parse_single_board/1)

    numbers = inp
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)

    {numbers, boards}
  end

  def transpose(rows) do
    rows
    |> List.zip
    |> Enum.map(&Tuple.to_list/1)
  end

  def check_row(r) do
    Enum.all?(r, &(&1==-1))
  end

  def check_board(b) do
    Enum.any?(Enum.map(b, &check_row/1)) or Enum.any?(Enum.map(transpose(b), &check_row/1))
  end

  def check_number(b, i) do
    Enum.map(b, fn x -> Enum.map(x, fn y -> if(y == i, do: -1, else: y) end) end)
  end

  def sum_remaining(b) do
    b
    |> List.flatten
    |> Enum.filter(&(&1!=-1))
    |> Enum.sum
  end

  def handle_boards_first_win({numbers, boards}), do: handle_boards_first_win(boards, numbers)
  def handle_boards_first_win(boards, [num | numbers]) do
    {wins, remaining_boards} = boards
    |> Enum.map(&check_number(&1, num))
    |> Enum.split_with(&check_board/1)

    if length(wins) > 0 do
      sum_remaining(hd wins) * num
    else
      handle_boards_first_win(remaining_boards, numbers)
    end
  end

  def handle_boards_last_win({numbers, boards}), do: handle_boards_last_win(boards, numbers)
  def handle_boards_last_win(boards, [num | numbers]) do
    {wins, remaining_boards} = boards
    |> Enum.map(&check_number(&1, num))
    |> Enum.split_with(&check_board/1)

    if remaining_boards == [] do
      sum_remaining(hd wins) * num
    else
      handle_boards_last_win(remaining_boards, numbers)
    end
  end

  @spec part1(binary) :: non_neg_integer
  def part1(file \\ "../day4/input.txt") do
    file
    |> Parse.parse_string_lines()
    |> parse_bingo_boards()
    |> handle_boards_first_win()
  end

  @spec part1(binary) :: non_neg_integer
  def part2(file \\ "../day4/input.txt") do
    file
    |> Parse.parse_string_lines()
    |> parse_bingo_boards()
    |> handle_boards_last_win()
  end
end
