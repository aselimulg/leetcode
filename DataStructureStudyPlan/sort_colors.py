# 75. Sort Colors
# medium
# https://leetcode.com/problems/sort-colors/

from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    two_pos = len(nums) - 1
    zero_pos = 0
    i = 0
    while i < len(nums):
        num = nums[i]
        if num == 0 and i != zero_pos:
            nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
            zero_pos += 1
        elif num == 2 and i < two_pos:
            nums[i], nums[two_pos] = nums[two_pos], nums[i]
            two_pos -= 1
        else:
            i += 1
    print(nums)

sortColors([2,0,2,1,1,0])