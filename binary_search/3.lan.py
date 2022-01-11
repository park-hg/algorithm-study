import sys

sys.stdin = open('input.txt', 'r')

K, N = map(int, sys.stdin.readline().rstrip().split())
lans = []
for _ in range(K):
    lans.append(int(sys.stdin.readline()))

left, right = 0, 1 << 32
while left < right:
    mid = (left + right) // 2
    nums = 0
    for lan in lans:
        nums += lan // mid
    if nums >= N:
        left = mid + 1
    else:
        right = mid

print(left-1)