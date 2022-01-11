import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

a, b, c = 0, 0, 0
def func(paper, n):
    global a, b, c
    if paper == [[paper[0][0]]*n for _ in range(n)]:
        if paper[0][0] == -1:
            a += 1
            return
        if paper[0][0] == 0:
            b += 1
            return
        if paper[0][0] == 1:
            c += 1
            return
            
    l = n // 3
    for i in range(3):
        for j in range(3):
            sub_paper = [paper[k][l*j:l*(j+1)] for k in range(l*i, l*(i+1))]
            func(sub_paper, l)

func(paper, N)
print(a)
print(b)
print(c)