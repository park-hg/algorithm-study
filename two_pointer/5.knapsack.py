import sys

sys.stdin = open('input.txt', 'r')

N, C = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

a, b = weights[:len(weights)//2], weights[len(weights)//2:]

def dfs(i, array, w, result):
    if i == len(array):
        result.append(w)
        return
    
    dfs(i+1, array, w, result)
    dfs(i+1, array, w+array[i], result)

a_list, b_list = [], []

dfs(0, a, 0, a_list)
dfs(0, b, 0, b_list)

b_list.sort()

cnt = 0
for w_a in a_list:
    target = C - w_a
    left, right = 0, len(b_list)
    while left < right:
        mid = (left + right) // 2
        if b_list[mid] <= target:
            left = mid + 1
        else:
            right = mid
    cnt += left

print(cnt)
