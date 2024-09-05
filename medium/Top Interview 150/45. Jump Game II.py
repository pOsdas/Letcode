def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    count = far = end_of_jump = 0

    for i in range(n - 1):
        far = max(far, i + nums[i])
        if i == end_of_jump:
            count += 1
            end_of_jump = far
            if end_of_jump >= n - 1:
                break

    return count
