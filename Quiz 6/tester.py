import sys

import lcs

answer = 'TCTGTTTTCCAGTGGTCTTCCGGCGATGATAATGACCTCCATAGCAATTGCAGGCGAGGTAAACGACAGAAATCCTTAAAAGACTGAGGCAGTGCTGGAACCGTGGTCAAACCACATGACCGGAGAACCACCACGGGTATCTTAGGCCATTCGCTTAGAGCGAGAAATCGCGCCATAAGGGCGAGGATACCCTAATAGTTTGATATCCGGTTCGCATCGTACGTATGTGGAAGAAAAACGGCTACGTGTGCGAGCGAAGTGGTTGTCGTGAGGCCAGAAGCTTATGGGCCCTGACCACCAGGACTAAGGTTGCCGAATCAGGCGTTGATTTACCAGCAACCCTCTAACCGAAAGCGGTGCACATCGTTTAGTCAGCGAAGTCCCCTGCCACGTTCGGGTTGGAGTGCTTACTTACCGCTGGCAGGCTGCGTCTAGTAAATTAGATTCTGGAGTTCCGAAGACAGGTGCTTTGGATCACAGTTTCGTAACCGCGAAGTGGTTGGCAGCAGTTAATTAGATACCTACCTCCAATATTCAAGTAAGGTTAAGTGCCGTCGAACCAGACATGGCTCCCCTTG'

with open('rosalind_ba5c.txt') as input_file:
    lines = input_file.readlines()

v = lines[0].strip()
w = lines[1].strip()
sys.setrecursionlimit(max(len(v), len(w)) * 2 + 1)
l = lcs.main(v, w)

if len(l) == len(answer):
    it = iter(v)
    if all(c in it for c in l):
        it = iter(w)
        if all(c in it for c in l):
            print('Passed.')
            exit()
    print('Fail.')
