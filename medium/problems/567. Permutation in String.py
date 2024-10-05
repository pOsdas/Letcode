class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        def check_matches(s1_count, s2_count) -> bool:
            for i in range(26):
                if s1_count[i] != s2_count[i]:
                    return False
            return True

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if check_matches(s1_count, s2_count):
                return True

            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

        return check_matches(s1_count, s2_count)
