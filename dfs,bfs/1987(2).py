import sys

sys.stdin = open('input.txt', 'r')

R, C = map(int, sys.stdin.readline().split())
grid = []
for _ in range(R):
    grid.append(list(sys.stdin.readline().rstrip()))

q = set([(0, 0, grid[0][0])])
cnt = 0
while q:
    print(q)
    x, y, d = q.pop()
    cnt = max(cnt, len(d))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] not in d:
            q.add((nx, ny, d+grid[nx][ny]))

print(cnt)