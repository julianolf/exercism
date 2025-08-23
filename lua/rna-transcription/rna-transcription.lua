local nucleotides = {
  ["A"] = "U",
  ["C"] = "G",
  ["G"] = "C",
  ["T"] = "A",
}

return function(dna)
  return dna:gsub("%a", nucleotides)
end
