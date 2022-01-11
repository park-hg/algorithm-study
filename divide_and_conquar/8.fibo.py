import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

def matmul(A, B):
    N = len(A)
    M = len(A[0])
    K = len(B[0])
    C = [[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for k in range(M):
                C[i][j] += (A[i][k]*B[k][j])%(10**9+7)
                C[i][j] %= (10**9+7)
    return C

def matpow(A, n):
    if n == 1:
        return A
    B = matpow(A, n//2)
    C = matmul(B, B)
    if n%2 == 1:
        return matmul(A, C)
    if n%2 == 0:
        return C

A = [[1, 1], [1, 0]]
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    A_n = matpow(A, n-1)
    print(A_n[0][0])