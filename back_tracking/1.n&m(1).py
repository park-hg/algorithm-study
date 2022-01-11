import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

def seq(sequence):
    if len(sequence) == M:
        print(*sequence)
        return
    for i in range(1, N+1):
        if i not in sequence:
            seq(sequence+[i])

seq([])