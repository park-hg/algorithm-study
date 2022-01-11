#n = int(input())
#grid = [list(map(int, input())) for _ in range(n)]

import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

grid = []
for _ in range(n):
    grid.append(list(map(int, list(sys.stdin.readline())[:n])))
visited = [[False] * n for _ in range(n)]

def dfs(i, j, cnt):
    global grid, visited
    stack = [[i, j]]
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True
            cnt += 1
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    stack.append([nx, ny])
    return cnt


results = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            results.append(dfs(i, j, 0))


print(results)