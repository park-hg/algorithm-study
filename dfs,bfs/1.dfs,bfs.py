import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n, m, v = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

graph = {k: sorted(v) for k, v in graph.items()}



def dfs(start_v):
    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in reversed(graph[v]):
                stack.append(w)
    return discovered

def bfs(start_v):
    discovered = [start_v]
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                # bfs는 큐에 넣기전 방문체크를 해야 메모리 초과가 안된다.
                discovered.append(w)
                queue.append(w)
    return discovered

print(*dfs(v))
print(*bfs(v))
