# N = 5
# arr = [1,2,3,4,5]
#
# for i in range(1<<N): # 1<<N 2**N
#    s = 0
#    for j in range(N):
#         if i & (1<<j):
#             s+=arr[j]
#
#             print(arr[j], end=' ')
#    print(s)

arr = [3,6,7,1,5,4]

n = len(arr) # 원소의 개수
N = int(input)
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):  # 0또는 0이 아닌???뭔소리야 졸리다.

            print(arr[j], end=", ")
    print()
print()
"""1<<n: 부분집합의 개수
원소의 수만큼 비트를 비교
i의 j번 비트가 1인 경우
j번 원소 출력력"""