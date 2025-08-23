local bob = {}

function bob.hey(say)
  local asking = say:sub(-1) == "?"
  local yelling = say:upper() == say
  local nothing = say:gsub("^%s*(.*)%s*$", "%1") == ""

  if nothing then
    return "Fine, be that way."
  elseif yelling and asking then
    return "Calm down, I know what I'm doing!"
  elseif asking then
    return "Sure"
  elseif yelling then
    return "Whoa, chill out!"
  else
    return "Whatever"
  end
end

return bob
