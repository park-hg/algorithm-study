import sys
import math
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
points, links = [], []
for _ in range(N):
    points.append(list(map(float, sys.stdin.readline().split())))
for _ in range(M):
    links.append(list(map(int, sys.stdin.readline().split())))
    
graph = [[0]*N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        graph[i][j] = graph[j][i] = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)

for i, j in links:
    graph[i-1][j-1] = graph[j-1][i-1] = 0

visited = [False] * N
visited[0] = True
i = 1
total_dist = 0
while i < N:
    min_dist = sys.maxsize
    for v in range(N):
        if visited[v]:
            for w in range(N):
                if not visited[w]:
                    if min_dist > graph[v][w]:
                        min_dist = graph[v][w]
                        next_v = w
    visited[next_v] = True
    total_dist += min_dist
    i += 1
print(f'{total_dist:.2f}')