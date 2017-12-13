def to_rna(dna_strand):
    rna_map = { 'G' : 'C',
                'C' : 'G',
                'T' : 'A',
                'A' : 'U'}
    ret = []
    for idx, d in enumerate(dna_strand):
        if d not in rna_map:
            raise ValueError("Invalid RNA nucleotide found at :" + str(d) )
        ret.append(rna_map[d])
    return ''.join(ret)
