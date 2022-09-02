# 136. Single Number
# easy
# https://leetcode.com/problems/single-number/

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum(set(nums)) * 2 - sum(nums)