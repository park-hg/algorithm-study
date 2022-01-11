import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    queue = deque([[0, 0, 1]])
    while queue:
        x, y, crush = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][crush]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][crush] == 0:
                    visited[nx][ny][crush] = visited[x][y][crush] + 1
                    queue.append([nx, ny, crush])
                elif graph[nx][ny] == 1 and crush == 1 and visited[nx][ny][crush] == 0:
                    visited[nx][ny][crush-1] = visited[x][y][crush] + 1
                    queue.append([nx, ny, crush-1])
    return -1

# visited를 2개로 나눠야 하는이유
# [nx, ny] 의 전 상태 [x, y]에서 crush=0, 1에 따라 
# visited[x][y]의 값이 다르고 
# 거기서 갱신된 visitied[nx][ny]의 값도 달라질 것이기 때문.
print(bfs())