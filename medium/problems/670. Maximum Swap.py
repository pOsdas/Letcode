class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        last = {int(d):i for i, d in enumerate(digits)}
        print(last)

        for i,d in enumerate(digits):
            for j in range(9, int(d), -1):
                if last.get(j, -1) > i:
                    digits[i], digits[last[j]] = digits[last[j]], digits[i]
                    return int(''.join(digits))

        return num
