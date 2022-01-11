import sys

sys.stdin = open('input.txt', 'r')

N, S = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

sum = 0
length = sys.maxsize
left, right = 0, 0

while True:
    if sum < S:
        if right == N:
            break
        else:
            sum += a[right]
            right += 1
    else:
        length = min(length, right-left)
        sum -= a[left]
        left += 1

if length == sys.maxsize:
    print(0)
else:
    print(length)