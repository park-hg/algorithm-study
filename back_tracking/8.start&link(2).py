import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [False] * N

scores = []
def dfs(idx, start, depth):
    if depth == N//2:
        scores.append(start)
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            temp = 0
            for j in range(0, i):
                if visited[j]:
                    temp += S[i][j] + S[j][i]
            start += temp
            dfs(i+1, start, depth+1)
            visited[i] = False
            start -= temp

dfs(0, 0, 0)

ans = sys.maxsize
print(scores)
for i in range((len(scores)-1)//2):
    start, link = scores[i], scores[len(scores)-1-i]
    ans = min(ans, abs(start-link))

print(ans)
    