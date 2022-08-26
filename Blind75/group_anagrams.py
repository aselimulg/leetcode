# 49. Group Anagrams
# medium
# https://leetcode.com/problems/group-anagrams/

from typing import Counter, List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = {}
    for i in strs:
        a = str(sorted(i))
        if a not in d:
            d[a] = [i]
        else:
            d[a].append(i)
    return d.values()