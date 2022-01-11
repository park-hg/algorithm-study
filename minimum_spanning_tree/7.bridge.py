import sys
import math
sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

def dfs(i, j):
    discovered = []
    stack = [[i, j]]
    grid[i][j] = 2
    while stack:
        x, y = stack.pop()
        discovered.append([x, y])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                stack.append([nx, ny])
                grid[nx][ny] = 2
    return discovered

islands = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            discovered = dfs(i, j)
            islands.append(discovered)

def dist(a, b):
    row, column = [], []
    
    for x, y in a:
        if x not in row:
            row.append(x)
        if y not in column:
            column.append(y)

    d = math.inf
    for x in row:
        d_row = math.inf
        for x_a, y_a in a:
            if x_a == x:
                for x_b, y_b in b:
                    if x_b == x:
                        cur_dist = abs(y_b-y_a)-1
                        ys, yt = min(y_a, y_b), max(y_a, y_b)
                        for j in range(ys+1, yt):
                            if grid[x][j] != 0:
                                cur_dist = math.inf
                        if 2 <= cur_dist < d_row:
                            d_row = cur_dist
        d = min(d_row, d)

    for y in column:
        d_col = math.inf
        for x_a, y_a in a:
            if y_a == y:
                for x_b, y_b in b:
                    if y_b == y:
                        cur_dist = abs(x_b-x_a)-1
                        xs, xt = min(x_a, x_b), max(x_a, x_b)
                        for i in range(xs+1, xt):
                            if grid[i][y] != 0:
                                cur_dist = math.inf
                        if 2 <= cur_dist < d_col:
                            d_col = cur_dist
        d = min(d_col, d)
    return d

num_i = len(islands)
visited = [False] * num_i
visited[0] = True
i = 1
total = 0
while i < num_i:
    next_v = 0
    cost = math.inf
    for v in range(num_i):
        if visited[v]:
            for w in range(num_i):
                if not visited[w]:
                    cur_cost = dist(islands[v], islands[w])
                    if cur_cost < cost:
                        cost = cur_cost
                        next_v = w
    visited[next_v] = True
    i += 1
    total += cost

if total == math.inf or not all(visited):
    print(-1)
else:
    print(total)
