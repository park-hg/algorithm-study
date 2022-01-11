import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
a.sort()

ans = 0
left, right = 0, len(a)-1
while left < right:
    if a[left] + a[right] > x:
        right -= 1
    elif a[left] + a[right] < x:
        left += 1
    else:
        ans += 1
        left += 1
        right -= 1

print(ans)