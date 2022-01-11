import sys
from collections import deque
import math
sys.stdin = open('input.txt', 'r')

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
grid = []
for _ in range(H):
    grid.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
hx = [2, 2, 1, 1, -1, -1, -2, -2]
hy = [1, -1, 2, -2, 2, -2, 1, -1]

q = deque([[0, 0, K]])
visited = [[[-1]*W for _ in range(H)] for _ in range(K+1)]
visited[K][0][0] = 0
ans = math.inf
while q:
    x, y, cnt = q.popleft()
    if x==H-1 and y==W-1:
        print(visited[cnt][x][y])
        exit()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < H and 0 <= ny < W and visited[cnt][nx][ny] == -1:
            if grid[nx][ny] != 1:
                visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                q.append([nx, ny, cnt])
    if cnt > 0:
        for i in range(8):
            nx, ny = x+hx[i], y+hy[i]
            if 0 <= nx < H and 0 <= ny < W and visited[cnt-1][nx][ny] == -1:
                if grid[nx][ny] != 1:
                    visited[cnt-1][nx][ny] = visited[cnt][x][y] + 1
                    q.append([nx, ny, cnt-1])
print(-1)