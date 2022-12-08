"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT


Sample Output
Rosalind_0808
60.919540

My slightly over engineered version below

Improvments to be made:
- Use something like start with [A-Z] to concat DNA string instead of editing file directly 
- investigate why stripped_fasta_out still has new line characters. 

"""
import argparse


def open_fasta(in_file):
    fasta_out = {}
    with open(in_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                fasta_out[line] = next(f)
    # strip newline and > characters
    stripped_fasta_out = {
        key.strip("\n>"): item.strip("/n") for key, item in fasta_out.items()
    }
    return stripped_fasta_out


def calc_gc_content(stripped_fasta_out):
    # count G/C content, get max, return max key value pair
    g_c_calc = {}
    for key, value in stripped_fasta_out.items():
        g_c_calc.update(
            {key: float((value.count("G") + value.count("C")) / len(value) * 100)}
        )
    # print([k for k,v in g_c_calc.items() if v ==  max(g_c_calc.values())][0], '\n', max(g_c_calc.values()))
    print(stripped_fasta_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_file", help=" an input file with id and DNA string on each line"
    )
    arguments = parser.parse_args()
    in_file = arguments.in_file
    stripped_fasta_out = open_fasta(in_file)
    calc_gc_content(stripped_fasta_out)
