import sys

sys.stdin = open('input.txt', 'r')

R, C = map(int, sys.stdin.readline().split())
grid = []
for _ in range(R):
    grid.append(list(sys.stdin.readline().rstrip()))

discovered = [False]*26
ans = 0
def dfs(x, y, discovered=discovered, cnt=1):
    global ans
    ans = max(ans, cnt)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not discovered[ord(grid[nx][ny])-65]:
                discovered[ord(grid[nx][ny])-65] = True
                dfs(nx, ny, discovered, cnt+1)
                discovered[ord(grid[nx][ny])-65] = False

discovered[ord(grid[0][0])-65] = True
dfs(0,0)
print(ans)