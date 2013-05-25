"""
The GC-content of a DNA string is given by the percentage of symbols in the
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.
Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A
commonly used method of string labeling is called FASTA format. In this
format, the string is introduced by a line that begins with '>', followed by
some labeling information. Subsequent lines contain the string itself; the
first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and
9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-
content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
"""

import os
from collections import OrderedDict

PATH = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))

"""
THIS IS NOT FULLY WORKING. PERCENT IS OFF BY .3 PROBABLY BC OF FATSA PARSING
"""


def fatsa(dataset="rosalind_gc.txt"):
    od = OrderedDict()
    db = open(PATH(dataset)).read().strip().splitlines()

    for idx in range(len(db)):
        # This is disgusting. Fix this hack
        if ">" in db[idx]:
            ctr = 1
            tmp = [db[idx+ctr]]
            try:
                while ">" not in db[idx+ctr]:
                    tmp.append(db[idx+ctr])
                    ctr += 1
            except IndexError:
                # EOF
                pass
            od[db[idx]] = "".join(tmp)
    return od


def gc_content(id, dna):
    gc = filter(lambda x: x in ["C", "G"], list(dna))
    return (len(gc)/float(len(list(dna)))) * 100


def render_answer(winner):
    return "%s\n%s" % (winner['id'].replace(">", ""), winner['percent'])


if __name__ == "__main__":
    db = fatsa()
    winner = {'id': "", 'dna': "", 'percent': 0.0}

    for k, v in db.items():
        percent = gc_content(k, v)
        if percent > winner['percent']:
            winner['percent'] = percent
            winner['id'] = k
            winner['dna'] = v

    print render_answer(winner)