RNA_codon_dict = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I ",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def open_fasta(in_file):
    """Open fasta file, if line starts with > skip and put next line in list"""
    dna_strings = []
    with open(in_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue
            dna_strings.append(line.strip("\n"))

    return dna_strings


def complement_string(s):
    "Returns the complement dna str for a str of dna"
    complement = []
    for dna_nucleotide in list(s):
        if dna_nucleotide.upper() == "G":
            dna_nucleotide = "C"
        elif dna_nucleotide.upper() == "A":
            dna_nucleotide = "T"
        elif dna_nucleotide.upper() == "T":
            dna_nucleotide = "A"
        elif dna_nucleotide.upper() == "C":
            dna_nucleotide = "G"
        complement.append(dna_nucleotide)

    return "".join(complement[::-1])
