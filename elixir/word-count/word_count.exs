defmodule Words do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    wc = fn wrd, acc -> Map.update(acc, wrd, 1, &(&1 + 1)) end

    String.downcase(sentence)
      |> String.split(~r/([^\w\d-]|_)/u, trim: true)
      |> Enum.reduce(Map.new(), wc)
  end
end

