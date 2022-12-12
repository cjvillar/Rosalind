"""
Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT
Sample Output
2 4 10
"""

# break s into substrings of len(t) and loop through to see if s.index(t) is true or if t == s in each


def motif(s, t):
    motif = []
    for i in range(len(s)):
        if t in s[i : i + len(t)]:
            motif.append(i + 1)  # i + 1 because we want 1 base start
    return " ".join(
        str(x) for x in motif
    )  # return in proper format (str with spaces) for Rosalind


# driver code
# s = 'GATATATGCATATACTT'
# t = 'ATAT'
s = "AACGGTAAAACGCTAACGGTATAAACGGTAAACGGTATAACGGTAAACGGTAGAGAACGGTAAACGGTAGGTAACGGTAGGAACGGTAAGAACGGTAGAACGGTAAAACGGTACATCAACGGTAAACGGTATAACGGTAAACGGTAGAAACGGTATTGAAACGGTACAAACGGTAGAACGGTATGGGAACGGTATAACGGTATCTAAACGGTATAACGGTATGAACGGTAAGGCAAACGGTAAAACGGTAAGGTGTATTGTAACGGTAAACGGTAGTAGGAACGGTAGGGGAACGGTATGAACGGTAAACGGTAAACGGTATTTTCATATCCAACGGTAGGTAACGGTATAACGGTAGTAACGGTAATGAACGGTAGGACTCGAAACGGTATAACGGTACGAAACAACGGTATAACGGTAGAACGGTAGAACGGTACAACGGTACGAACGGTACTTGTTCCCGGAACGGTAAACGGTAAGCGAACGGTATCAAAAAACGGTACAACGGTACTATTCAACGGTACGGAACGGTATTCTCGAACGAACGGTAAACGGTAACCCAATGGTTGACAACGGTATTAGCAACGGTAACCCATAACCGTTGTTAACGGTAAACGGTAAAAACGGTATGGTTGAACGGTAAACGGTAAACGGTACAAACGGTAAACGGTAGCGGGAAACGGTACCCGGCAACCGAACGGTAGGCAGCCTCTGCAATATAACGGTAGTGGAAGAACGGTAAAGTATACAGAGGAACGGTACCCGCCAAAAGAACGGTATAGTAACGGTAAAACGGTACGAGAACGGTATTTTAACGGTATCCTTGGGGAGGTTGTAAAACGGTAATGAGGAACGGTAAACGGTATCAAACGGTAGGATAACGGTAATAACGCAACGGTAAACGGTATAACGGTACTAAACGGTAAACGGTAAACGGTA"
t = "AACGGTAAA"
# ans = [1, 24, 39, 56, 99, 118, 133, 236, 262, 301, 308, 465, 544, 607, 614, 636, 643, 659, 735, 784, 852, 894, 919, 926]
print(motif(s, t))
