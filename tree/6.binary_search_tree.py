import sys

sys.stdin = open('input.txt', 'r')

pre = []

line = sys.stdin.readline().rstrip()
while line:
    pre.append(int(line))
    line = sys.stdin.readline().rstrip()


def post(pre):
    if pre:
        node = pre[0]
        idx = len(pre)+1
        for i in range(1, len(pre)):
            if pre[i] > node:
                idx = i
                break
        post(pre[1:idx])
        post(pre[idx:])
        print(node)
    
post(pre)