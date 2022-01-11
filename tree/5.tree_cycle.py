import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

idx = [0]*(n+1)
for i in range(n):
    idx[in_order[i]] = i

def preorder(in_s, in_e, post_s, post_e):
    if in_e > in_s:
        node = post_order[post_e-1]
        print(node, end= ' ')
        node_idx = idx[node]
        preorder(in_s, node_idx, post_s, node_idx+post_s-in_s)
        preorder(node_idx+1, in_e, node_idx+post_s-in_s, post_e-1)

preorder(0, len(in_order), 0, len(post_order))