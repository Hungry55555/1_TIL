import sys
sys.stdin = open('input.txt')
arr = []
N = int(input())
# for _ in range(N):
#     arr.append(list(map(int, input().split())))
# print(arr)
#리스트 컴프리헨션 기본 형태 [표현식 for _ in range(N)], 임시 변수는 표현식 내부에서 사용가능합니다.
arr2 = [list(map(int, input().split())) for _ in range(N)] # [표현식, 표현식, list(map(int, input().split())))]
print(arr2)