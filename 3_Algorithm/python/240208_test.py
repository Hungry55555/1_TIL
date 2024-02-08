def f(i, k):
    if i == k:
        print('end')
    else:
        f(i+1,k)
f(0,1000)
# 이런경우는 최대함수 깊이를 초과해서 불가능 이런경우는 재귀로 다루지 않는다
