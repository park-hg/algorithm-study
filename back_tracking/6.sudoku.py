import sys

sys.stdin = open('input.txt', 'r')

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            zeros.append([i, j])

def candidate(point):
    i, j = point
    candidates = list(range(1, 10))
    for k in range(9):
        if grid[i][k] in candidates:
            candidates.remove(grid[i][k])
        if grid[k][j] in candidates:
            candidates.remove(grid[k][j])
    i, j = (i//3)*3, (j//3)*3
    for x in range(3):
        for y in range(3):
            if grid[i+x][j+y] in candidates:
                candidates.remove(grid[i+x][j+y])
    return candidates

flag = False
def dfs(i):
    global flag
    # 답을 1개만 찾으면 되므로 flag 정의
    # return 대신 exit()써도 됨
    if flag:
        return

    if i == len(zeros):
        for row in grid:
            print(*row)
        flag = True
        return 
    
    for num in candidate(zeros[i]):
        grid[zeros[i][0]][zeros[i][1]] = num
        dfs(i+1)
        grid[zeros[i][0]][zeros[i][1]] = 0

dfs(0)