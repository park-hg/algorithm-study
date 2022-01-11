import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
n_plus, n_minus, n_mul, n_div = map(int, sys.stdin.readline().split())

ans = []
def dfs(i, p, m, mul, div, eq):
    if i == N-1:
        ans.append(eq)
        return
    if p < n_plus:
        dfs(i+1, p+1, m, mul, div, eq+A[i+1])
    if m < n_minus:
        dfs(i+1, p, m+1, mul, div, eq-A[i+1])
    if mul < n_mul:
        dfs(i+1, p, m, mul+1, div, eq*A[i+1])
    if div < n_div:
        if eq < 0:
            dfs(i+1, p, m, mul, div+1, -(abs(eq)//A[i+1]))
        else:
            dfs(i+1, p, m, mul, div+1, eq//A[i+1])

dfs(0, 0, 0, 0, 0, A[0])           
print(max(ans))
print(min(ans))