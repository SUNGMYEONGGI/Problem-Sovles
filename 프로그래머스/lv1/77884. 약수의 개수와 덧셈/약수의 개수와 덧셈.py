def solution(left, right):
    cnt = 0
    answer = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
            cnt = 0
        elif cnt % 2 != 0:
            answer -= i
            cnt = 0
    return answer