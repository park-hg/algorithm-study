import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

def prime_list(n):
    a = [False, False] + [True]*(n-1)
    primes = []
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

primes = prime_list(N)
left, right = 0, 0
sum = 0
cnt = 0
while right <= len(primes):
    if sum >= N:
        if sum == N:
            cnt += 1
        sum -= primes[left]
        left += 1
    else:
        if right == len(primes):
            break
        sum += primes[right]
        right += 1         

print(cnt)