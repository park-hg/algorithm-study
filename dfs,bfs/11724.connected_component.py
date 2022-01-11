import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
graph = [[0]*N for _ in range(N)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1][v-1] = graph[v-1][u-1] = 1

visited = [False] *N


def dfs(i):
    visited[i] = True
    for j in range(N):
        if not visited[j] and graph[i][j]:
            dfs(j)

cnt = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)