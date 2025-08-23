return {
  decode = function(c1, c2, c3)
    local bands = {
      black = 0,
      brown = 1,
      red = 2,
      orange = 3,
      yellow = 4,
      green = 5,
      blue = 6,
      violet = 7,
      grey = 8,
      white = 9,
    }

    local value = (bands[c1] * 10 + bands[c2]) * (10 ^ bands[c3])
    local unit = 'ohms'

    if value >= 1000 then
      value = value / 1000
      unit = 'kiloohms'
    end

    return value, unit
  end
}
