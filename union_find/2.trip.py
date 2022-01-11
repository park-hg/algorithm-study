import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

par = list(range(N))
rank = [0] * N

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
        return
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
        return

def same(trip):
    for i in range(len(trip)-1):
        if find(trip[i]-1) != find(trip[i+1]-1):
            print("NO")
            return
    print("YES")
    return

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if l[j] == 1:
            unite(i, j)

trip = list(map(int, sys.stdin.readline().split()))
same(trip)
