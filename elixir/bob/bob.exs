defmodule Bob do
  defp is_question(msg), do: String.ends_with?(msg, "?")

  defp is_yelling(msg) do
    String.match?(msg, ~r/[^\d\W]/u) and msg == String.upcase(msg)
  end

  defp is_yelling_question(msg) do
    is_yelling(msg) and is_question(msg)
  end

  def hey(input) do
    cond do
      String.trim(input) == "" ->
        "Fine. Be that way!"
      is_yelling_question(input) ->
        "Calm down, I know what I'm doing!"
      is_yelling(input) ->
        "Whoa, chill out!"
      is_question(input) ->
        "Sure."
      true ->
        "Whatever."
    end
  end
end
