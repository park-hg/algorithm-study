import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

M, N = map(int, sys.stdin.readline().split())
grid = []
for _ in range(M):
    grid.append(list(map(int, sys.stdin.readline().split())))
visited = [[-1]*N for _ in range(M)]

def dfs(x, y):
    if visited[x][y] == -1:
        visited[x][y] = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] < grid[x][y]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]

visited[-1][-1] = 1
print(dfs(0,0))