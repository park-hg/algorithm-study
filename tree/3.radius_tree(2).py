import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
graph = {i:[] for i in range(n)}
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])

visited = [False] * n
dist = [0] * n
def dfs(v):
    visited[v] = True
    for w, d in graph[v]:
        if not visited[w]:
            dist[w] = dist[v] + d
            dfs(w)

dfs(0)

start_v = dist.index(max(dist))
visited = [False] * n
dist = [0] * n
dfs(start_v)
print(max(dist))