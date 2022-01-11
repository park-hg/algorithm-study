import sys

sys.stdin = open('input.txt', 'r')

a, b, c = map(int, sys.stdin.readline().rstrip().split())

a_list = []
a_bin = []

def power(a, b):
    if b == 1:
        return a%c
    p = power(a, b//2)
    if b%2 == 0:
        return p*p%c
    if b%2 == 1:
        return a*p*p%c

print(power(a, b))