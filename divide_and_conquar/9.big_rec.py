import sys
import math

sys.stdin = open('input.txt', 'r')

def init(array, tree, node, start, end):
    if start == end:
        tree[node] = start
        return
    mid = (start+end) // 2
    init(array, tree, node*2, start, mid)
    init(array, tree, node*2+1, mid+1, end)
    if array[tree[node*2]] <= array[tree[node*2+1]]:
        tree[node] = tree[node*2]
    else:
        tree[node] = tree[node*2+1]
    return

def query(array, tree, node, start, end, left, right):
    if end < left or start > right:
        return -1
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start+end) // 2
    left_q = query(array, tree, node*2, start, mid, left, right)
    right_q = query(array, tree, node*2+1, mid+1, end, left, right)
    if left_q == -1:
        return right_q
    elif right_q == -1:
        return left_q
    elif array[left_q] <= array[right_q]:
        return left_q
    else:
        return right_q

def get_area(array, tree, start, end):
    n = len(array)
    idx = query(array, tree, 1, 0, n-1, start, end)
    area = (end-start+1)*array[idx]
    if start < idx:
        temp = get_area(array, tree, start, idx-1)
        area = max(area, temp)
    if idx < end:
        temp = get_area(array, tree, idx+1, end)
        area = max(area, temp)
    return area

while True:
    T = list(map(int, sys.stdin.readline().rstrip().split()))
    if T == [0]:
        break
    n, T = T[0], T[1:]
    h = math.ceil(math.log2(n))
    tree = [0] * (1 << (h+1))
    init(T, tree, 1, 0, n-1)
    print(get_area(T, tree, 0, n-1))