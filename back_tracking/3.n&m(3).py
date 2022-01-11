import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

def func(seq):
    if len(seq) == M:
        print(*seq)
        return
    for i in range(1, N+1):
        func(seq+[i])

func([])