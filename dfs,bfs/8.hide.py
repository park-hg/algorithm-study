import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n, k = map(int, sys.stdin.readline().split())

time = [0] * 100001
queue = deque([n])

while queue:
    x = queue.popleft()
    if x == k:
        print(time[k])
        break
    d = [-1, 1, x]
    for dx in d:
        nx = x + dx
        if 0 <= nx < 100001 and time[nx] == 0:
            queue.append(nx)
            time[nx] = time[x] + 1