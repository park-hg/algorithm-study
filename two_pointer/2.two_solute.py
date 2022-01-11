import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

left, right = 0, len(a)-1
a_1, a_2 = a[left], a[right]

while left < right:
    if a[left] + a[right] < 0:
        if abs(a[left] + a[right]) < abs(a_1 + a_2):
            a_1, a_2 = a[left], a[right]
        left += 1
    elif a[left] + a[right] > 0:
        if abs(a[left] + a[right]) < abs(a_1 + a_2):
            a_1, a_2 = a[left], a[right]
        right -= 1
    else:
         a_1, a_2 = a[left], a[right]
         break

print(a_1, a_2)