N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())
    if r+c==e:
        print('does not matter')
    elif r+c > e:
        print('do not advertise')
    else:
        print('advertise')