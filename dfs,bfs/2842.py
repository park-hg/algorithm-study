import sys
import math
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
height = []
for _ in range(N):
    height.append(list(map(int, sys.stdin.readline().split())))

homes = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'P':
            p = (i, j)
        elif graph[i][j] == 'K':
            homes += 1

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

h = []
for i in range(N):
    for j in range(N):
        if height[i][j] not in h:
            h.append(height[i][j])
h.sort()
print(h)
ans = math.inf
left, right = 0, 0
while left <= right:
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    print(left, right)
    if h[left] <= height[p[0]][p[1]] <= h[right]:
        visited[p[0]][p[1]] = True
        stack = [p]
        while stack:
            x, y = stack.pop()
            if graph[x][y] == 'K':
                cnt += 1
            for i in range(8):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if h[left] <= height[nx][ny] <= h[right]:
                        visited[nx][ny] = True
                        stack.append([nx, ny])
    if cnt == homes:
        ans = min(ans, h[right]-h[left])
        left += 1
    else:
        if right == len(h)-1:
            break
        right += 1
print(ans)