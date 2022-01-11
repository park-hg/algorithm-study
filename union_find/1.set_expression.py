import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

par = list(range(n+1))
rank = [0] * (n+1)

def find(x):
    if par[x] == x:
        return x
    return find(par[x])

def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x, y):
    return find(x) == find(y)

for _ in range(m):
    q, x, y = map(int, sys.stdin.readline().split())
    if q == 0:
        unite(x-1, y-1)
    elif q == 1:
        if same(x-1, y-1):
            print("YES")
        else:
            print("NO")
            