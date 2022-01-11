#binary search의 뼈대 알고리즘

# 최소 인덱스를 return
def bisect_left(a, x):
    # lo, hi 는 func의 정의역 -1/+1
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        # key point
        # func(mid)가 x의 증가함수 이면 <, 감소함수이면 >
        if condition(func(mid), x):
            lo = mid + 1
        else:
            hi = mid
    return lo

# 최대 인덱스를 return
def bisect_right(a, x):
    # lo, hi 는 func의 정의역 -1/+1
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        # key point
        # func(mid)가 x의 증가함수 이면 <=, 감소함수이면 >=
        if condition(func(mid), x):
            lo = mid + 1
        else:
            hi = mid
    return lo

# func가 일대일 대응이면 bisect_left == bisect_right