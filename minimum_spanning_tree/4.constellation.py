import sys
import math
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    s.append(list(map(float, sys.stdin.readline().split())))

graph = [[0]*n for _ in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        graph[i][j] = graph[j][i] = math.sqrt((s[i][0]-s[j][0])**2 + (s[i][1]-s[j][1])**2)

visited = [False] * n
visited[0] = True
total_cost = 0
i = 1
while i < n:
    cost = sys.maxsize
    for v in range(n):
        if visited[v]:
            for w in range(n):
                if not visited[w]:
                    if cost > graph[v][w]:
                        cost = graph[v][w]
                        next_v = w
    total_cost += cost
    visited[next_v] = True
    i += 1

print(total_cost)
