# 1. Two Sum
# easy
# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_map = dict()
    for i, v in enumerate(nums):
        if target - v in nums_map:
            return [nums_map[target- v], i]
        nums_map[v] = i