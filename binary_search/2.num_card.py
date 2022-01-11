import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

card.sort()

def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_right(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo

print(*[bisect_right(card, target)-bisect_left(card, target) for target in nums])

