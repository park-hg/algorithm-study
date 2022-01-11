import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

def is_prime(x):
    i = 2
    while i*i <= x:
        if x%i == 0:
            return False
        i += 1
    return True

primes = []
for i in range(2, N+1):
    if is_prime(i):
        primes.append(i)

left, right = 0, 0
sum = 0
ans = 0
while True:
    if sum < N:
        if right == len(primes):
            break
        else:
            sum += primes[right]
            right += 1
    elif sum == N:
        ans += 1
        sum -= primes[left]
        left += 1
    else:
        sum -= primes[left]
        left += 1

print(ans)