import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

cnt = 1
seq = [1000001]

for i in range(len(A)):
    if A[i] > seq[-1]:
        seq.append(A[i])
        cnt += 1
    else:
        left, right = 0, len(seq)-1
        # bisect_left를 써야 A[i]가 seq에 있든 없든 결과가 같다.
        while left < right:
            mid = (left + right) // 2
            if seq[mid] < A[i]:
                left = mid + 1
            else:
                right = mid
        seq[left] = A[i]

print(cnt)