import sys
import math

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

points = []
for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().rstrip().split())))
points.sort()


def distance(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2

def func(array):
    if len(array) == 1:
        return math.inf
    if len(array) == 2:
        return distance(*array)
    
    mid = (len(array)-1) // 2
    dist = min(func(array[:mid+1]), func(array[mid:]))
    temp_array = []
    for i in range(mid-1, -1, -1):
        if (array[mid][0] - array[i][0])**2 < dist:
            temp_array.append(array[i])
        else:
            break
    for i in range(mid+1, len(array)):
        if (array[mid][0] - array[i][0])**2 < dist:
            temp_array.append(array[i])
        else:
            break
    temp_array.sort(key=lambda x:x[1])
    for i in range(len(temp_array)-1):
        for j in range(i+1, len(temp_array)):
            if (temp_array[i][1] - temp_array[j][1])**2 < dist:
                dist = min(dist, distance(temp_array[i], temp_array[j]))
            else:
                break
    
    return dist

print(func(points))