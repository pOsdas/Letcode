class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        remember_i = []
        remember_j = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    remember_i.append(i)
                    remember_j.append(j)

        for i in range(rows):
            for j in range(cols):
                if i in remember_i or j in remember_j:
                    matrix[i][j] = 0


