import heapq

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
def solution(operations):
    max_heap, min_heap = [], []
    for query in operations:
        q, n = query.split()
        n = int(n)
        if q == 'I':
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
        elif q == 'D':
            if n == 1:
                if max_heap:
                    x = -heapq.heappop(max_heap)
                    min_heap.remove(x)
            elif n == -1:
                if min_heap:
                    x = -heapq.heappop(min_heap)
                    max_heap.remove(x)
    if max_heap:
        mx = -heapq.heappop(max_heap)
    else:
        mx = 0
    if min_heap:
        mn = heapq.heappop(min_heap)
    else:
        mn = 0
    return [mx, mn]

solution(operations)