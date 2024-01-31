"""
3
123
456
789
"""

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)] # for _ in range(N) dms ekstns qksqhrdml dmlalfh _sms rmwj qustnsl ekfmsrjffh eocp rksmd
# arr2 = [[0]*N for _ in range(N)]
# arr3 =[[0]*N]*N # 얕은복사를 해서 저렇게 하면 안된다.
# print(arr3)
# arr3[0][0]=1
# print(arr3)

# 델타ㅠㅠ
N = 5
arr = [[0]*N for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0 <=nj<N:
                print(arr[ni][nj], end = ' ')
        print()

