import sys

sys.stdin = open('input.txt', 'r')

n, k= map(int, sys.stdin.readline().rstrip().split())
p = int(1e9 + 7)

fac = [1]*(n+1)
for i in range(1, n+1):
    fac[i] = (fac[i-1]*i) % p
    
a = fac[n]
b = (fac[n-k] * fac[k]) % p
print((a * pow(b, p-2, p)) % p)