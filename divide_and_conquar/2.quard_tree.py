import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

image = []
for _ in range(N):
    image.append(list(sys.stdin.readline().rstrip()))

def zipper(grid):
    global answer
    l = len(grid)
    if grid == [['1']*l for _ in range(l)]:
        return '1'
    if grid == [['0']*l for _ in range(l)]:
        return '0'

    first = [grid[i][:l//2] for i in range(l//2)]
    second = [grid[i][l//2:] for i in range(l//2)]
    third = [grid[i][:l//2] for i in range(l//2, l)]
    fourth = [grid[i][l//2:] for i in range(l//2, l)]

    first = zipper(first)
    second = zipper(second)
    third = zipper(third)
    fourth = zipper(fourth)

    return "(" + first + second + third + fourth + ")"

print(zipper(image))