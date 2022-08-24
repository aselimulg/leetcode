# 326. Power of Three
# easy
# https://leetcode.com/problems/power-of-three/
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    if n == 1:
        return True
    while n > 1:
        if n % 3 != 0:
            return False
        n /= 3
    return True