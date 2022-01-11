import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()

def binary_search(target, left, right):
    if left <= right:
        mid = (left + right) // 2
        if A[mid] > target:
            return binary_search(target, left, mid-1)
        elif A[mid] < target:
            return binary_search(target, mid+1, right)
        else:
            return 1
    return 0


for target in T:
    print(binary_search(target, 0, len(A)-1))