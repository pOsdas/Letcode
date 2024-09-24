class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        s = set()
        for x in arr1:
            while x:
                s.add(x)
                x //= 10
        ans = 0
        for x in arr2:
            while x:
                if x in s:
                    ans = max(ans, len(str(x)))
                    break
                x //= 10
        return ans