import sys
import heapq

sys.stdin = open('input.txt', 'r')

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = {i:{} for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        graph[u][v] = min(w, graph[u][v])
    else:
        graph[u][v] = w




dist = [sys.maxsize] * (V+1)
dist[K] = 0
heap = [(0, K)]
while heap:
    cur_dist, v = heapq.heappop(heap)
    # 현재 pop된것이 최소거리가 아니면 갱신 의미 없음.
    if cur_dist > dist[v]:
        continue
    for w in graph[v]:
        if cur_dist + graph[v][w] < dist[w]:
            dist[w] = cur_dist + graph[v][w]
            heapq.heappush(heap, (dist[w], w))


for d in dist[1:]:
    if d == sys.maxsize:
        print("INF")
    else:
        print(d)