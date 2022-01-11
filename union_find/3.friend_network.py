import sys

sys.stdin = open('input.txt', 'r')

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
        num[y] += num[x]
    else:
        par[y] = x
        num[x] += num[y]
        if rank[x] == rank[y]:
            rank[x] += 1

T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    par = list(range(2*F))
    rank = [0] * 2*F
    num = [1] * 2*F
    friends = dict()
    cnt = 0
    for _ in range(F):
        name1, name2 = sys.stdin.readline().split()
        if name1 not in friends:
            friends[name1] = cnt
            cnt += 1
        if name2 not in friends:
            friends[name2] = cnt
            cnt += 1
        unite(friends[name1], friends[name2])
        print(num[find(friends[name2])])