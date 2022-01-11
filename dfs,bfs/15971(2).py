import sys

sys.stdin = open('input.txt', 'r')
N, s, t = map(int, sys.stdin.readline().split())
s, t = s-1, t-1
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])

# 경로가 유일하므로 dfs로 풀 수 있다.

visited = [False] * N
stack = [[s, 0, 0]]
while stack:
    v, d, e = stack.pop()
    if v == t:
        break
    visited[v] = True
    for w, cost in graph[v]:
        if not visited[w]:
            stack.append([w, d+cost, max(e, cost)])

print(d-e)

def dfs(s, t, cost, edge):
    if s == t:
        print(cost, edge)
        exit()
        
    visited[s] = True
    for v, c in graph[s]:
        if not visited[v]:
            return dfs(v, t, cost+c, max(edge, c))

dfs(s, t, 0, 0)