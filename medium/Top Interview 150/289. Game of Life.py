class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1),
        ]

        copy_board = [[board[i][j] for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                live = 0

                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < cols:
                        live += copy_board[ni][nj]

                if board[i][j] == 1:  # live
                    if live < 2 or live > 3:
                        board[i][j] = 0

                else:  # dead
                    if live == 3:
                        board[i][j] = 1
