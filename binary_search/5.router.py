import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

N, C = map(int, sys.stdin.readline().split())
x = []
for _ in range(N):
    x.append(int(sys.stdin.readline()))

x.sort()

def func(mid):
    cur = x[0]
    cnt = 1
    for i in range(1, N):
        if x[i] - cur >= mid:
            cur = x[i]
            cnt += 1
    return cnt

left, right = 0, max(x)+1 #func의 정의역의 범위 +1 -1을 써야한다
while left < right:
    mid = (left + right) // 2
    if func(mid) >= C:
        left = mid + 1
    else:
        right = mid

print(left-1)