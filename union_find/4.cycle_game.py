import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

par = list(range(n))
rank = [0] * n

def find(x):
    if x == par[x]:
        return x
    return find(par[x])

def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return True
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def same(x, y):
    return find(x) == find(y)

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if same(x, y):
        print(i+1)
    else:
        unite(x, y)

print(0)