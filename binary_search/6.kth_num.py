import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

def func(x):
    y = 0
    for i in range(1, N+1):
        y += min(x//i, N)
    return y

left, right = 0, N**2+1
while left < right:
    mid = (left + right) // 2
    if func(mid) < k:
        left = mid + 1
    else:
        right = mid

print(left)