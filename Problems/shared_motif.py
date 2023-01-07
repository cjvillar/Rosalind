"""
Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC


"""
import argparse


def open_fasta(in_file):
    dna_strings = []
    with open(in_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue
            dna_strings.append(line.strip("\n"))

    return dna_strings


def find_motif(stripped_fasta_out):
    # get length of first common substring then look for a longer one
    for dna_string in stripped_fasta_out:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_file", help=" an input file with id and DNA string on each line"
    )
    arguments = parser.parse_args()
    in_file = arguments.in_file
    stripped_fasta_out = open_fasta(in_file)
    find_motif(stripped_fasta_out)
