import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

R, C = map(int, sys.stdin.readline().split())
grid = []
for _ in range(R):
    grid.append(list(sys.stdin.readline().rstrip()))

fire = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'J':
            p = [i, j]
        elif grid[i][j] == 'F':
            fire.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque([p+[0]])
fire = deque(fire)
cur_time = -1
while q:
    x, y, time = q.popleft()
    if x==0 or x==R-1 or y==0 or y==C-1:
        print(time+1)
        exit()
    if time > cur_time:
        len_fire = len(fire)
        while len_fire:
            fx, fy = fire.popleft()
            for i in range(4):
                fnx, fny = fx+dx[i], fy+dy[i]
                if 0 <= fnx < R and 0 <= fny < C and grid[fnx][fny] != '#' and grid[fnx][fny] != 'F':
                    grid[fnx][fny] = 'F'
                    fire.append([fnx, fny])
            len_fire -= 1
        cur_time = time
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':
            grid[nx][ny] = 'J'
            q.append([nx, ny, time+1])
print('IMPOSSIBLE')