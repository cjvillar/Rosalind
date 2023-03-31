"""
Genes are Discontiguous

In “Transcribing DNA into RNA”, we mentioned that a strand of DNA is copied into a strand of RNA during transcription, but we neglected to mention how transcription is achieved.

In the nucleus, an enzyme (i.e., a molecule that accelerates a chemical reaction) called RNA polymerase (RNAP) initiates transcription by breaking the bonds joining complementary bases of DNA. It then creates a molecule called precursor mRNA, or pre-mRNA, by using one of the two strands of DNA as a template strand: moving down the template strand, when RNAP encounters the next nucleotide, it adds the complementary base to the growing RNA strand, with the provision that uracil must be used in place of thymine; see Figure 1.

Because RNA is constructed based on complementarity, the second strand of DNA, called the coding strand, is identical to the new strand of RNA except for the replacement of thymine with uracil. See Figure 2 and recall “Transcribing DNA into RNA”.

After RNAP has created several nucleotides of RNA, the first separated complementary DNA bases then bond back together. The overall effect is very similar to a pair of zippers traversing the DNA double helix, unzipping the two strands and then quickly zipping them back together while the strand of pre-mRNA is produced.

For that matter, it is not the case that an entire substring of DNA is transcribed into RNA and then translated into a peptide one codon at a time. In reality, a pre-mRNA is first chopped into smaller segments called introns and exons; for the purposes of protein translation, the introns are thrown out, and the exons are glued together sequentially to produce a final strand of mRNA. This cutting and pasting process is called splicing, and it is facilitated by a collection of RNA and proteins called a spliceosome. The fact that the spliceosome is made of RNA and proteins despite regulating the splicing of RNA to create proteins is just one manifestation of a molecular chicken-and-egg scenario that has yet to be fully resolved.

In terms of DNA, the exons deriving from a gene are collectively known as the gene's coding region.

Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s
 (of length at most 1 kbp) and a collection of substrings of s
 acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s
. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset:
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

MVYIADKQHVASREAYGHMFKVCA

Thoughts:
Need RNA to protein dictionary created in rna_to_splicing.py.

"""

import argparse


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


def parse_data(fasta_in):
    "get max srting as DNA and substrings as introns"
    substrings = []
    for seq in fasta_in:
        if seq == max(fasta_in):  # longest str is the "dna"
            dna = seq
        substrings.append(seq)  # create list of substrings aka "intons"
    substrings.remove(dna)  # remove "dna" from "introns" list
    return dna, substrings


# TODO remove "intron" substrings. revisit method
def remove_introns(dna, substrings):
    "Loop through dna and removee substrings"
    i = 0
    exons = dna
    while i < len(substrings):
        exons = exons.replace(substrings[i], "")
        i += 1
    return exons


def transcribe(dna):
    "Translate the T in dna to U for rna"
    exons = dna
    RNA = []
    for i in exons:
        if i == "T":
            i = "U"
        RNA.append(i)

    rna = "".join(RNA)

    return rna


def rna_to_protien(rna):
    "loop through every 3 rna letters and look up key: value in RNA_codon_dict"
    s = rna
    # translate rna to protein
    protein = []
    for i in range(0, len(s), 3):
        protein.append(RNA_codon_dict.get(s[i : i + 3]))

    return "".join([str(i) for i in protein])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_file", help=" an input file with id and DNA string on each line"
    )
    arguments = parser.parse_args()
    in_file = arguments.in_file
    fasta_in = open_fasta(in_file)
    dna, substrings = parse_data(fasta_in)
    exons = remove_introns(dna, substrings)
    rna = transcribe(exons)
    print(rna_to_protien(rna))
