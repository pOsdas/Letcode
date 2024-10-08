def canJump(nums):
    current = 0

    for i in range(len(nums)):
        if i > current:
            return False

        current = max(current, i + nums[i])

        if current >= len(nums) - 1:
            return True

    return False
