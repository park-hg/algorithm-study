import sys
import math
sys.stdin = open('input.txt', 'r')
N, S = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

sum = 0
left, right = 0, 0
length = math.inf
while left <= right <= N:
    if sum >= S:
        length = min(length, right-left)
        sum -= a[left]
        left += 1     
    else:
        if right == N:
            break
        sum += a[right]
        right += 1

if length == math.inf:
    print(0)
else:
    print(length)