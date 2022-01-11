import math

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class segment_tree:
    def __init__(self):
        self.H = math.ceil(math.log2(len(A)))
        self.tree = [0]*(1 << (self.H + 1))

    def fit(self, A, node=1, start=0, end=len(A)-1):
        if start == end:
            self.tree[node] = A[start]
            return self.tree[node]
        self.tree[node] = self.fit(A, node*2, start, (start+end)//2)+self.fit(A, node*2+1, (start+end)//2+1, end)
        return self.tree[node]
     
    def sum(self, left, right, node=1, start=0, end=len(A)-1):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        return self.sum(node*2, start, (start+end)//2, left, right) + self.sum(node*2+1, (start+end)//2+1, end, left, right)

    def update(self, index, val, node=1, start=0, end=len(A)-1):
        if index < start or index > end:
            return
        self.tree[node] += (val - self.A[index])
        if start != end:
            self.update(node*2, start, (start+end)//2, index, val)
            self.update(node*2+1, (start+end)//2+1, end, index, val)

seg_tree = segment_tree()
seg_tree.fit(A)
print(seg_tree.tree)
print(seg_tree.sum(0, 5))