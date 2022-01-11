import sys

sys.stdin = open('input.txt', 'r')

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    pos = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, sys.stdin.readline().split())
        pos[j][i] = 1
    
    def dfs(i, j):
        stack = [[i, j]]
        while stack:
            x, y = stack.pop()
            if pos[x][y] == 1:
                pos[x][y] = 0
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and pos[nx][ny] == 1:
                        stack.append([nx, ny])
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if pos[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)