defmodule Bob do
  defp nothing?(msg), do: String.trim(msg) == ""

  defp question?(msg), do: String.ends_with?(msg, "?")

  defp yelling?(msg) do
    String.downcase(msg) != msg and msg == String.upcase(msg)
  end

  def hey(input) do
    cond do
      nothing?(input) ->
        "Fine. Be that way!"
      yelling?(input) and question?(input) ->
        "Calm down, I know what I'm doing!"
      yelling?(input) ->
        "Whoa, chill out!"
      question?(input) ->
        "Sure."
      true ->
        "Whatever."
    end
  end
end
