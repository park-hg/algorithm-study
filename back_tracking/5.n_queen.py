import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

board = [0] * N
cnt = 0

def dfs(n):
    global cnt
    def condition(i):
        for j in range(n):
            if i == board[j] or i == board[j]+n-j or i == board[j]-n+j:
                return False
        return True  
    if n == N:
        cnt += 1
        return
    for i in range(N): 
        if condition(i):
            board[n] = i
            dfs(n+1)

dfs(0)
print(cnt)