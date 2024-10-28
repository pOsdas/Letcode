from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        num_set = set(nums)
        max_length = -1

        for num in nums:
            length = 0
            current = num

            while current in num_set:
                length += 1
                current = current ** 2

            if length >= 2:
                max_length = max(max_length, length)

        return max_length if max_length >= 2 else -1
