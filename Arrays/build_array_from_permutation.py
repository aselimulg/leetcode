# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        for i, x in enumerate(nums):
            ans[i] = nums[x]
        return ans