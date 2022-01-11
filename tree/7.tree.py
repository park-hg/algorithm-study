import sys

sys.stdin = open('input.txt', 'r')

def dfs(start_v):
    is_tree = True
    stack = [start_v]
    while stack:
        print(stack)
        v = stack.pop()
        if visited[v]:
            is_tree = False
        else:
            visited[v] = True
            for w in graph[v]:
                if not visited[w]:
                    stack.append(w)
    return is_tree

line = sys.stdin.readline().rstrip()
case_num = 1
while line:
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    graph = {i:[] for i in range(n)}
    visited = [0] * n
    T = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[b-1].append(a-1)
        graph[a-1].append(b-1)
    print(graph)
    for i in range(n):
        if not visited[i]:
            ans = dfs(i)
            print(ans)
            if ans:
                T += 1
    if T > 1:
        print(f"Case {case_num}: A forest of {T} trees.")
    elif T == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: No trees.")
    case_num += 1
    line = sys.stdin.readline().rstrip()
