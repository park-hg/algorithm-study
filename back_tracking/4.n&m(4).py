import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

def func(seq):
    if len(seq) == M:
        print(*seq)
        return
    for i in range(1, N+1):
        if not seq or seq[-1] <= i:
            func(seq+[i])

func([])