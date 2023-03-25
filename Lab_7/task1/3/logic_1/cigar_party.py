def cigar_party(cigars, is_weekend):
    return ((is_weekend or cigars >= 60) and cigars >= 40)
