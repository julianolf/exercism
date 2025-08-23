def to_rna(dna_strand=''):
    dna = dna_strand.upper()
    trans_table = str.maketrans('GCTA', 'CGAU')
    return dna.translate(trans_table)
