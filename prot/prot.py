"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from
the English alphabet (all letters except for B, J, O, U, X, and Z).

Protein strings are constructed from these 20 symbols. Henceforth, the term
genetic string will incorporate protein strings along with DNA strings and RNA
strings.

The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10
kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
MAMAPRTEINSTRING
"""

import re
import sys
from itertools import takewhile

RNA_CODON_TBL = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
"""


def prot(seq):
    codons = re.findall("...", seq)
    rna_codons = RNA_CODON_TBL.split()
    codon_map = dict(zip(rna_codons[::2], rna_codons[1::2]))
    return takewhile(lambda v: v.lower() != 'stop', map(codon_map.get, codons))

if __name__ == '__main__':
    with open('rosalind_prot.txt') as fh:
        print("".join(prot(fh.read())))
    sys.exit(0)
