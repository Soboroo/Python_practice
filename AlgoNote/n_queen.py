# N-queen
board = [[0 for i in range(8)] for j in range(8)]


def n_queen(n):
    def is_valid(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def dfs(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                dfs(row + 1)
                board[row] = -1

    board = [-1] * n
    result = []
    dfs(0)
    return result

print(n_queen(8))