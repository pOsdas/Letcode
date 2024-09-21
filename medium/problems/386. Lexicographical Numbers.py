def lexicalOrder(self, n: int) -> list[int]:
    result = []
    current = 1

    for i in range(n):
        result.append(current)
        if current * 10 <= n:
            current *= 10
        elif current % 10 != 9 and current + 1 <= n:
            current += 1
        else:
            while (current // 10) % 10 == 9:
                current //= 10
            current = current // 10 + 1

    return result
