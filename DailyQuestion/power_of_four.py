# 342. Power of Four
# easy
# https://leetcode.com/problems/power-of-four/

def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 10 != 4 and n % 10 != 6:
        return False
    while n % 4 == 0:
        n = n / 4
    
    if n == 1:
        return True
    else:
        return False

