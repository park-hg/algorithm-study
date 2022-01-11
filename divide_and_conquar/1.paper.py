import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

white, blue = 0, 0

def color(grid):
    global white, blue
    l = len(grid)
    if grid == [[0]*l for _ in range(l)]:
        white += 1
        return
    if grid == [[1]*l for _ in range(l)]:
        blue += 1
        return

    first = [grid[i][:l//2] for i in range(l//2)]
    second = [grid[i][:l//2] for i in range(l//2, l)]
    third = [grid[i][l//2:] for i in range(l//2)]
    fourth = [grid[i][l//2:] for i in range(l//2, l)]

    color(first)
    color(second)
    color(third)
    color(fourth)

color(paper)
print(white)
print(blue)