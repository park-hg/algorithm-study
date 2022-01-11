import sys

sys.stdin = open('input.txt', 'r')

V = int(sys.stdin.readline())
graph = {i:[] for i in range(V)}
for _ in range(V):
    l = list(map(int, sys.stdin.readline().split()))
    a, l = l[0], l[1:]
    for i in range(0, len(l)-1, 2):
        graph[a-1].append([l[i]-1, l[i+1]])

visited = [False] * V
dist = [0] * V

def dfs(v):
    visited[v] = True
    for w, d in graph[v]:
        if not visited[w]:
            dist[w] = dist[v] + d
            dfs(w)

dfs(0)

start_v = dist.index(max(dist))
visited = [False] * V
dist = [0] * V
dfs(start_v)
print(max(dist))