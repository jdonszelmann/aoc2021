defmodule Aoc2021.Parse do
  def parse_int_lines(file) do
    File.read!(file)
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  def parse_string_lines(file) do
    File.read!(file)
    |> String.split("\n", trim: true)
  end

  def split_to_integers(line) do
    line
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
    |> Enum.to_list()
  end

end
