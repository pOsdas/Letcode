def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # first version
    # O(n) - fastest
    n = len(nums)
    output = [1] * n

    left = 1
    for i in range(n):
        output[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    # second
    # O(n^2) - slower
    n = len(nums)
    output = [1] * n
    for i in range(n):
        for j in range(n):
            if nums[j] != nums[i]:
                output[i] *= nums[j]

    return output