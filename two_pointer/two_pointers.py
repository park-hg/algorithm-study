# two pointers의 뼈대 알고리즘

#한쪽 방향에서 시작할 때
#만약 condition이 재귀적으로 update 가능하면 left, right update시에 같이 계산
left, right = 0, 0
while left <= right:
    if condition(left, right):
        left += 1
    else:
        if right == len(A)-1:
            break
        right += 1

#양쪽 끝에서 시작할 때
left, right = 0, len(A)-1
while left != right:
    if condition(left, right):
        left += 1
    else:
        right -= 1