import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
p = []
for i in range(N):
    p.append(list(map(int, sys.stdin.readline().split()))+[i])

par = list(range(N))
rank = [0] * N

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

edges = []
for i in range(3):
    p.sort(key=lambda x:x[i])
    for j in range(1, N):
        edges.append([p[j][-1], p[j-1][-1], abs(p[j-1][i]-p[j][i])])
edges.sort(key=lambda x:x[-1])

total = 0
for x, y, cost in edges:
    if not same(x, y):
        unite(x, y)
        total += cost

print(total)