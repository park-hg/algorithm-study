import sys
import math

sys.stdin = open('input.txt', 'r')

N, M, K = map(int, sys.stdin.readline().rstrip().split())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))

def init(array):
    h = math.ceil(math.log2(len(A)))
    tree = [0] * (1 << (h+1))
    for i in range(1, len(A)+1):
        l = i & -i
        tree[i] = sum(array[i-l:i])
    return tree

def update(tree, i, diff):
    while i < len(tree):
        tree[i] += diff
        i += (i&-i)

def summation(tree, start, end):
    start -= 1
    sum_s, sum_e = 0, 0
    while start > 0:
        sum_s += tree[start]
        start -= (start&-start)
    while end > 0:
        sum_e += tree[end]
        end -= (end&-end)
    return sum_e - sum_s

fenwick_tree = init(A)
for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        update(fenwick_tree, b, c-A[b-1])
        A[b-1] = c
    elif a == 2:
        print(summation(fenwick_tree, b, c))