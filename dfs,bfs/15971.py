import sys
import heapq
import math
sys.stdin = open('input.txt', 'r')
N, s, t = map(int, sys.stdin.readline().split())
s, t = s-1, t-1
tree = {i:{} for i in range(N)}
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a-1][b-1] = c
    tree[b-1][a-1] = c

def dijkstra(s, t):
    distance = [math.inf]*N
    distance[s] = 0
    prev = [-1] * N

    heap = [(0, s)]
    while heap:
        current_dis, v = heapq.heappop(heap)
        if v == t:
            return distance[t], prev
        if distance[v] < current_dis:
            continue
        for w in tree[v]:
            if distance[w] < current_dis + tree[v][w]:
                continue
            else:
                distance[w] = current_dis + tree[v][w]
                prev[w] = v
                heapq.heappush(heap, (distance[w], w))

dist, prev = dijkstra(s, t)
p = t
max_edge = 0
while p != s:
    max_edge = max(max_edge, tree[p][prev[p]])
    p = prev[p]

print(dist-max_edge)
