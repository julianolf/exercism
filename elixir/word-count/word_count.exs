defmodule Words do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    String.downcase(sentence)
      |> String.replace(~r/[^\w\d\s-]/u, "")
      |> String.split(~r/[\s_]/u, trim: true)
      |> Enum.reduce(Map.new(), fn wrd, acc -> Map.update(acc, wrd, 1, &(&1 + 1)) end)
  end
end
