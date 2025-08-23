defmodule Lasagna do
  @oven_time 40
  @layer_time 2
  @alarm_message "Ding!"

  def expected_minutes_in_oven, do: @oven_time

  def remaining_minutes_in_oven(minutes) do
    abs(expected_minutes_in_oven() - minutes)
  end

  def preparation_time_in_minutes(layers) do
    @layer_time * layers
  end

  def total_time_in_minutes(layers, minutes_in_oven) do
    preparation_time_in_minutes(layers) + minutes_in_oven
  end

  def alarm, do: @alarm_message
end
