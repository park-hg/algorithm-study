import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(i, j):
    visited[i][j] = True
    q = deque([[i, j]])
    #ice_cnt = 1
    zeros = []
    while q:
        x, y = q.popleft()
        zero_cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y +dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] != 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    #ice_cnt += 1
                else:
                    zero_cnt += 1
        if zero_cnt:
            zeros.append([x, y, zero_cnt])
    #return ice_cnt, zeros
    return zeros


ans = 0
while True:
    visited = [[False]*M for _ in range(N)]
    zeros = []
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j] and not visited[i][j]:
                zeros.extend(bfs(i, j))
                cnt += 1
    if cnt == 0:
        ans = 0
        break
    if cnt > 1:
        break
    for i, j, c in zeros:
        grid[i][j] -= c
        if grid[i][j] < 0:
            grid[i][j] = 0
    ans += 1
print(ans)
'''
ans = 0
ice = []
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0:
            ice.append([i, j])
while True:
    if len(ice) == 0:
        ans = 0
        break
    cnt, zeros = bfs(ice[0][0], ice[0][1])
    if cnt != len(ice):
        break
    for i, j, c in zeros:
        grid[i][j] -= c
        if grid[i][j] <= 0:
            grid[i][j] = 0
            if ice:
                ice.remove([i, j])
    ans += 1
print(ans)'''

