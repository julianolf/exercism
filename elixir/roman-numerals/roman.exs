defmodule Roman do
  @num [{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}]

  defp convert(number, {_, _}) when number == 0, do: {0, ""}
  defp convert(number, {divisor, repr}) do
    times = div(number, divisor)
    {divisor * times, String.duplicate(repr, times)}
  end

  @doc """
  Convert the number to a roman number.
  """
  @spec numerals(pos_integer) :: String.t()
  def numerals(number) do
    if number > 3000, do: throw(number)

    Enum.reduce(@num, {0, ""}, fn num, acc ->
      {diff, repr} = acc
      {d, r} = convert(number - diff, num)
      {diff + d, repr <> r}
    end)
      |> elem(1)
  end
end
