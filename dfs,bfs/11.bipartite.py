import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

k = int(sys.stdin.readline())
for _ in range(k):
    vv, e = map(int, sys.stdin.readline().split())
    graph = {i:[] for i in range(vv)}
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visited = [0] * vv
    ans = True
    for i in range(vv):
        if visited[i] == 0:
            visited[i] = 1
            queue = deque([i])
            while queue:
                v = queue.popleft()
                for w in graph[v]:
                    if visited[w] == visited[v]:
                        ans = False
                    elif visited[w] == 0:
                        visited[w] = -visited[v]
                        queue.append(w)         
               
    print("YES" if ans else "NO")

    # 왜 함수로 쓰면 안되지