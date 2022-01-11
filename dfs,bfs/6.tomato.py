import sys
import math
from collections import deque

sys.stdin = open('input.txt', 'r')

m, n = map(int, sys.stdin.readline().split())

grid = []
queue = deque([])
for i in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if grid[i][j] == 0:
            grid[i][j] = math.inf
        elif grid[i][j] == 1:
            grid[i][j] = 0       
            queue.append([i, j, 0])     

def bfs():
    while queue:
        x, y, dist = queue.popleft()
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and dist + 1 < grid[nx][ny]:
                grid[nx][ny] = dist + 1
                queue.append([nx, ny, dist + 1])

bfs()
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == math.inf:
            print(-1)
            exit(0)
    ans = max(ans, max(grid[i]))
print(ans)