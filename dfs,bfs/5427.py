import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(p, fire):
    q = deque([p+[0]])
    fire = deque(fire)
    cur_time = -1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, time = q.popleft()
        if x==h-1 or x==0 or y==w-1 or y==0:
            return time+1
        if time > cur_time:
            len_fire = len(fire)
            while len_fire:
                fx, fy = fire.popleft()
                for i in range(4):
                    fnx, fny = fx+dx[i], fy+dy[i]
                    if 0 <= fnx < h and 0 <= fny < w and grid[fnx][fny] != '#' and grid[fnx][fny] != '*':
                        grid[fnx][fny] = '*'
                        fire.append([fnx, fny])
                len_fire -= 1
            cur_time = time
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == '.':
                grid[nx][ny] = '@'
                q.append([nx, ny, time+1])
    return 'IMPOSSIBLE'

T = int(sys.stdin.readline())
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(h):
        grid.append(list(sys.stdin.readline().rstrip()))
    
    fire = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                p = [i, j]
            elif grid[i][j] == '*':
                fire.append([i, j])
    print(bfs(p, fire))