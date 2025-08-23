import gleam/int

const oven_time = 40

const layer_time = 2

pub fn expected_minutes_in_oven() -> Int {
  oven_time
}

pub fn remaining_minutes_in_oven(minutes_in_oven: Int) -> Int {
  int.absolute_value(oven_time - minutes_in_oven)
}

pub fn preparation_time_in_minutes(layers: Int) -> Int {
  layer_time * layers
}

pub fn total_time_in_minutes(layers: Int, minutes_in_oven: Int) -> Int {
  preparation_time_in_minutes(layers) + minutes_in_oven
}

pub fn alarm() -> String {
  "Ding!"
}
