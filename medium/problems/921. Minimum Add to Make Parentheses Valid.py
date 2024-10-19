class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close_need = 0
        open_need = 0

        for char in s:
            if char == "(":
                close_need += 1
            elif char == ")":
                if close_need > 0:
                    close_need -= 1
                else:
                    open_need += 1

        return close_need + open_need
