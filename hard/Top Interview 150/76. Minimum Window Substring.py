from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window_count = dict()

        left = 0
        min_length = float('inf')
        min_window = ""
        have, need = 0, len(t_count)

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]

                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        return min_window


# s = Solution()
# print(s.minWindow("ADOBECODEBANC", "ABC"))
