n = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort(reverse=True)
B_list.sort()
result = 0

for i in range(n):
    result += (A_list[i] * B_list[i])
print(result)