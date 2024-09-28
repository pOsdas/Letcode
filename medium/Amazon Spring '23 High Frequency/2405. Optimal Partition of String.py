class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        position = 1

        for char in s:
            if char in seen:
                position += 1
                seen.clear()

            seen.add(char)

        return position
