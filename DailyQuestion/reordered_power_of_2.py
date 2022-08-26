# 869. Reordered Power of 2
# medium
# https://leetcode.com/problems/reordered-power-of-2/


import itertools


def reorderedPowerOf2(n: int) -> bool:
    return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1 
    for cand in itertools.permutations(str(n)))