def solution(a, b):
    answer = 0
    
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            answer += i
        return answer
    elif a < b:
        for j in range(a, b+1):
            answer += j
        return answer
            