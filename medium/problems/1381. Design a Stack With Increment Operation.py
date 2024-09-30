class CustomStack:

    def __init__(self, maxSize: int):
        self.data: list = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.data) < self.maxSize:
            self.data.append(x)

    def pop(self) -> int:
        if len(self.data) > 0:
            return self.data.pop(-1)
        return -1

    def increment(self, k: int, val: int) -> None:
        # if len(self.data) >= k:
        #     for i in range(k):
        #         self.data[i] += val
        # else:
        #     for i in range(len(self.data)):
        #         self.data[i] += val
        """faster"""
        limit = min(k, len(self.data))
        for i in range(limit):
            self.data[i] += val
