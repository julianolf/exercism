local nucleotides = {
  ["A"] = "U",
  ["C"] = "G",
  ["G"] = "C",
  ["T"] = "A",
}

return function(dna)
  local rna = ""

  for nucleotide in dna:gmatch("(.)") do
    rna = rna .. nucleotides[nucleotide]
  end

  return rna
end
