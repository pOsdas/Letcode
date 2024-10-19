class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(n: str) -> str:
            return ''.join('1' if char == '0' else '0' for char in n)

        def reverse(n: str) -> str:
            return n[::-1]

        def get_s(n: int) -> str:
            if n == 1:
                return '0'

            s = '0'
            for i in range(2, n + 1):
                s = s + "1" + reverse(invert(s))

            return s

        n = get_s(n)
        return n[k - 1]
