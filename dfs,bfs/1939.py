import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(dict)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if b-1 not in graph[a-1]:
        graph[a-1][b-1] = c
    else:
        graph[a-1][b-1] = max(graph[a-1][b-1], c)
    if a-1 not in graph[b-1]:
        graph[b-1][a-1] = c
    else:
        graph[b-1][a-1] = max(graph[b-1][a-1], c)
s, t = map(int, sys.stdin.readline().split())
s, t = s-1, t-1

def bfs(s, t, x):
    q = deque([[s, 0]])
    visited = [False]*N
    visited[s] = True
    while q:
        v, _ = q.popleft()
        if v == t:
            return True
        for w in graph[v]:
            if not visited[w] and graph[v][w] >= x:
                visited[w] = True
                q.append([w, graph[v][w]])
    return False

left, right = 0, 10**9+1
while left < right:
    mid = (left + right) // 2
    if bfs(s, t, mid):
        left = mid+1
    else:
        right = mid
print(left-1)