return function(dna)
  local rna = ""
  local nucleotides = {
    ["A"] = "U",
    ["C"] = "G",
    ["G"] = "C",
    ["T"] = "A",
  }

  for nucleotide in dna:gmatch("(.)") do
    rna = rna .. nucleotides[nucleotide]
  end

  return rna
end
