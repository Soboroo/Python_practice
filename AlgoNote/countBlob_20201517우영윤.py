def countCells(x, y):
    if x < 0 or y < 0 or x >= 8 or y >= 8 or visited[x][y] or cells[x][y] == 0:
        return 0
    dx = [0, 0, 1, 1, -1, -1, 1, -1]
    dy = [1, -1, 1, -1, 1, -1, 0, 0]
    visited[x][y] = True
    result = 1
    for i in range(8):
        result += countCells(x + dx[i], y + dy[i])
    return result


visited = [[False for _ in range(8)] for _ in range(8)]
cells = [[0, 0, 1, 0, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 1, 0, 0],
         [0, 1, 1, 0, 0, 0, 1, 1]]

print(countCells(3, 5))
