import sys

sys.stdin = open('input.txt', 'r')

n, k= map(int, sys.stdin.readline().rstrip().split())
p = int(1e9 + 7)

fac = [1]
inv = [0, 1]
facinv = [1, 1]
for i in range(n):
    fac.append(fac[-1]*(i+1))

for i in range(2, max(k, n-k)+1):
    inv.append((-inv[p%i]*(p//i))%p)
    facinv.append(facinv[-1]*inv[i])
    

comb = fac[n] * facinv[n-k] * facinv[k] % p
print(comb)