# 53. Maximum Subarray
# medium
# https://leetcode.com/problems/maximum-subarray/


def maxSubArray(nums):
    """
    type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    sum = 0

    for x in nums:
        sum += x
        if max_sum < sum:
            max_sum = sum
        if sum <= 0:
            sum = 0

    return max_sum


def maxSubArray2(nums):
    """
    type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    start_pos = 0
    while start_pos < len(nums):
        sum = 0
        for x in nums[start_pos:]:
            sum += x
            if max_sum < sum:
                max_sum = sum

        start_pos += 1

    return max_sum
