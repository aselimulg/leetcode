# 383. Ransom Note
# easy
# https://leetcode.com/problems/ransom-note/

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for letter in ransomNote:
        if letter not in magazine:
            return False
        magazine = magazine.replace(letter, '', 1)
    return True



def canConstruct2(ransomNote: str, magazine: str) -> bool:
        def getDict(string):
            d = dict()
            for letter in string:
                d[letter] = d.get(letter, 0) + 1
            return d
        ransomNote_dict = getDict(ransomNote)
        magazine_dict = getDict(magazine)
        magazine.replace()
        for k, v in ransomNote_dict.items():
            if magazine_dict.get(k, 0) < v:
                return False
        return True

print(canConstruct('aa', 'ab'))