import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

parent = [0] * N
visited = [False]*N
graph = {i:[] for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent[0] = 1
visited[0] = True 
stack = [1]
while stack:
    v = stack.pop()
    for w in graph[v]:
        if not visited[w-1]:
            visited[w-1] = True
            stack.append(w)
            parent[w-1] = v
            
for i in parent[1:]:
    print(i)