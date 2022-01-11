import sys

sys.stdin = open('input.txt', 'r')

N, S = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

sum = 0
length = sys.maxsize
left, right = 0, 0

while right <= N:
    if sum >= S:
        length = min(length, right-left)
        sum -= a[left]
        left += 1
    else:
        if right == N:
            break
        sum += a[right]
        right += 1

print(length)