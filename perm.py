"""
A permutation of length n is an ordering of the positive integers {1,2,...,n}. For example, x=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n <= 7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""


def gen_list(n=3):
    return "".join(map(str, [x for x in range(1, n + 1)]))


def permute(s):
    if len(s) <= 1:
        return s

    perm = permute(s[1:])
    c = s[0]
    r = []

    for p in perm:
        for i in range(len(p) + 1):
            r.append(p[:i] + c + p[i:])

    return r


perm = permute(gen_list(n=5))
for p in perm:
    print " ".join(map(str, p))
