def f(pat, txt, M, N):
    for i in range(N-M+1):  # text에서 비교 시작 위치, break하면 여기로 돌아옴
        for j in range(M):
            if txt[i+j] != pat[j]:  # 불일치면 다음 시작위치로
                break
        else:       # 패턴 매칭에 성공하면 for문이 잘 완료됐으면!
            return 1
    # 모든 위치에서 비교가 끝난경우
    return 0


T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)        # j는 0,1,2를 바복하고 i는 i-3까지??

    ans = f(pat,txt,M,N)
    print(f'#{tc} {ans}')

    