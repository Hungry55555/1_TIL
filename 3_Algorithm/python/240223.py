# def sec(k):
#     print(k^1004)
#
# sec(4)
# sec(1000)
# sec(1007)
# sec(3)
# for i in range(5):
#     print(bin(0b1<<i),0b1<<i)
#
# t=1
# for i in range(5):
#     print(bin(t),t)
#     t=t<<1
T= int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    result = 'ON'
    for i in range(N):
        if M&(1<<i)==(1<<i):
            pass
        else:
            result='OFF'
            break
    print(f'#{tc} {result}')