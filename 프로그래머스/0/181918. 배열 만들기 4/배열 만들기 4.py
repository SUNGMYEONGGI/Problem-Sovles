def solution(arr):
    stk = []
    i = 0
    while True:
        if i == len(arr):
            break
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            elif stk[-1] >= arr[i]:
                stk.pop()
    return stk