import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(t)+1


def bisect_left(start, end):
    if start < end:
        mid = (start + end) // 2
        ans = 0
        for i in t:
            if i > mid:
                ans += (i-mid)
        if ans >= M:
            return bisect_left(mid+1, end)
        else:
            return bisect_left(start, mid)
    return start-1

print(bisect_left(left, right))