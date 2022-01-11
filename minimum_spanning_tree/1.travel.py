import sys
sys.stdin = open('input.txt', 'r')

def find(x):
    if x == par[x]:
        return x
    return find(par[x])

def unite(x, y):
    x, y = find(x), find(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x, y):
    return find(x) == find(y)

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    par = list(range(N))
    rank = [0] * N
    cnt = 0
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if not same(a-1, b-1):
            unite(a-1, b-1)
            cnt += 1
    print(cnt)