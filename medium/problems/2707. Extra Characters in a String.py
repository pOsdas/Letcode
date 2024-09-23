class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        dictionary = set(dictionary)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]


