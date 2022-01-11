import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')


tickets = []
for _ in range(9):
    tickets.append(list(sys.stdin.readline().rstrip().split()))
N = len(tickets)
graph = defaultdict(list)
for a, b in tickets:
    graph[a].append(b)
for key in graph:
    graph[key].sort()

def dfs(v, path):
    if len(path) == N+1:
        return path
    for i in range(len(graph[v])):
        country = graph[v].pop(i)
        ret = dfs(country, path+[country])
        graph[v].insert(i, country)
        if ret:
            return ret

print(dfs("ICN", ["ICN"]))

