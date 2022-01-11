import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

t = int(sys.stdin.readline())

delta = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

def bfs(s, e):
    queue = deque([s])
    while queue:
        x, y = queue.popleft()
        if x == e[0] and y == e[1]:
            return grid[x][y]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                queue.append([nx, ny])

for _ in range(t):
    l = int(sys.stdin.readline())
    grid = [[0]*l for _ in range(l)]
    s = list(map(int, sys.stdin.readline().split()))
    e = list(map(int, sys.stdin.readline().split()))
    print(bfs(s, e))