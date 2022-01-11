import sys
import heapq
sys.stdin = open('input.txt', 'r')

V, E = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(V)}
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append([c, a-1, b-1])
    graph[b-1].append([c, b-1, a-1])

visited = [False] * V
visited[0] = True
heap = graph[0]
heapq.heapify(heap)
ans = 0
while heap:
    cost, u, v = heapq.heappop(heap)
    if not visited[v]:
        ans += cost
        visited[v] = True
        for edge in graph[v]:
            if not visited[edge[2]]:
                heapq.heappush(heap, edge)
print(ans)

