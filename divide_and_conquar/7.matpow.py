import sys

sys.stdin = open('input.txt', 'r')

N, b = map(int, sys.stdin.readline().rstrip().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

def matmul(A, B):
    N = len(A)
    M = len(A[0])
    K = len(B[0])
    C = [[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for k in range(M):
                C[i][j] += (A[i][k]*B[k][j])%1000
                C[i][j] %= 1000
    return C

def matpow(A, n):
    for i in range(len(A)):
        A[i] = [a%1000 for a in A[i]]
    if n == 1:
        return A
    B = matpow(A, n//2)
    C = matmul(B, B)
    if n%2 == 1:
        return matmul(A, C)
    if n%2 == 0:
        return C

for row in matpow(A, b):
    print(*row)