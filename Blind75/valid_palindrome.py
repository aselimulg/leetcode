# 125. Valid Palindrome
# easy
# https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s: str) -> bool:
    lower_word = s.lower()
    lower_word = ''.join([l for l in lower_word if l.isalnum()])
    if lower_word[::-1] == lower_word:
        return True
    return False

print(isPalindrome("A man, a plan, a canal: Panama"))