import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

discovered = []
stack = [1]

while stack:
    v = stack.pop()
    if v not in discovered:
        discovered.append(v)
        for w in graph[v]:
            stack.append(w)

print(len(discovered)-1)