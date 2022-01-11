import sys
import math

sys.stdin = open('input.txt', 'r')

N, M, K = map(int, sys.stdin.readline().rstrip().split())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))

class segment_tree:
    def __init__(self, A):
        self.A = A
        self.H = math.ceil(math.log2(len(A)))
        self.tree = [0]*(1 << (self.H + 1))

    def fit(self, node=1, start=0, end=len(A)-1):
        if start == end:
            self.tree[node] = self.A[start]
            return self.tree[node]
        self.tree[node] = self.fit(node*2, start, (start+end)//2)+self.fit(node*2+1, (start+end)//2+1, end)
        return self.tree[node]
     
    def sum(self, left, right, node=1, start=0, end=len(A)-1):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        return self.sum(left, right, node*2, start, (start+end)//2) + self.sum(left, right, node*2+1, (start+end)//2+1, end)

    def update(self, index, val, node=1, start=0, end=len(A)-1):
        if index < start or index > end:
            return
        self.tree[node] += (val - self.A[index])
        if start != end:
            self.update(index, val, node*2, start, (start+end)//2)
            self.update(index, val, node*2+1, (start+end)//2+1, end)

seg_tree = segment_tree(A)
seg_tree.fit()
print(seg_tree.tree)
for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        seg_tree.update(b-1, c)
        A[b-1] = c
    elif a == 2:
        print(seg_tree.sum(b-1, c-1))