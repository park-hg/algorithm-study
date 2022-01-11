import sys
import math
sys.stdin = open('input.txt', 'r')

def dist(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

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

N, M = map(int, sys.stdin.readline().split())
p, l = [], []
for i in range(N):
    p.append(list(map(float, sys.stdin.readline().split())))
for _ in range(M):
    l.append(list(map(int, sys.stdin.readline().split())))

edges = []
for i in range(N-1):
    for j in range(i+1, N):
        edges.append([i, j, dist(p[i], p[j])])

edges.sort(key=lambda x:x[-1])

par = list(range(N))
rank = [0]*N
for x, y in l:
    unite(x-1, y-1)

total = 0
for x, y, d in edges:
    if not same(x, y):
        unite(x, y)
        total += d
print(f'{total:.2f}')