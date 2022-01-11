import sys

sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

dp = [[0]*M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False]*M for _ in range(N)]
ans = 0
def dfs(x, y, cnt=1):
    global ans
    ans = max(ans, cnt)
    n = int(graph[x][y])
    for i in range(4):
        nx, ny = x+n*dx[i], y+n*dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 'H':
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                if dp[nx][ny] < cnt+1:
                    dp[nx][ny] = cnt+1
                    visited[nx][ny] = True
                    dfs(nx, ny, cnt+1)
                    visited[nx][ny] = False
dfs(0, 0)
print(ans)