import sys
sys.stdin = open('input.txt', 'r')


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    