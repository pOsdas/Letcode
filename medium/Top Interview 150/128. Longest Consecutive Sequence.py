class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_count = 0
        nums = set(nums)

        for num in nums:
            if (num - 1) not in nums:
                count = 1
                while num + 1 in nums:
                    count += 1
                    num += 1
                max_count = max(max_count, count)

        return max_count
