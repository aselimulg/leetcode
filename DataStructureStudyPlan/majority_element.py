def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sorted(nums)[int(len(nums) / 2)]