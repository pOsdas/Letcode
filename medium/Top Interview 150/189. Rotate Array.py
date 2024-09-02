def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
