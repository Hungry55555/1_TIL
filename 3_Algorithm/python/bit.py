arr = ['a','b','c','d']
N = len(arr)

# arr에 대한 모든 경우의 수

for i in range(1<<N):   #모든 부분집합을 뽑기 위한 반복 (4비트로 표현 가능) 2의 4승으로 표현할 수 있는 숫자는 0~15까지 표현 가능 16은 자릿수가 달라서 아님
    # arr의 idx
    for j in range(N): #비트는 왼쪽에서 오른쪽으로 자리가 증가를 하기 때문에 0 1 2 3 번 비트 비트의 자릿수와 = arr에서 사용하는 각 요소 의미
        print('='*30)   #j:해당 비트의 자리가 1인지 확인하기 위해 쉬프트를 하는 역할
        # i :모든 경우의 수 중,  i번째
        # ㅑ ==