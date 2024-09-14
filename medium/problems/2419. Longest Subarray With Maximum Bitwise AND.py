def longestSubarray(nums: list[int]) -> int:
    if not nums:
        return 0

    count = max_count = 0
    compare = max(nums)
    for num in nums:
        if num == compare:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0

    return max_count