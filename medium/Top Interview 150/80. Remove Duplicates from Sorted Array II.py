def removeDuplicates(nums: list):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return len(nums)

    j = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1

    while j < len(nums):
        nums[j] = '_'
        j += 1

    return nums

# print(removeDuplicates([1,1,1,2,2,3]))

