# 217. Contains Duplicate
# easy
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    sorted_nums = sorted(nums)
    for i, x in enumerate(sorted_nums[:-1]):
        if x == sorted_nums[i + 1]:
            return True
    return False

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashMap = {}
    for i in range(len(nums)):
        if hashMap.get(nums[i]) == None:
            hashMap[nums[i]] = i
        else:
            return True
    return False
