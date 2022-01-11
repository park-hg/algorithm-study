import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().rstrip().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

M, K = map(int, sys.stdin.readline().rstrip().split())
B = []
for _ in range(M):
    B.append(list(map(int, sys.stdin.readline().rstrip().split())))

C = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(*row)