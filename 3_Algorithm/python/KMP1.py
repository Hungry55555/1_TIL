def kmp(t, p):
    N = len(t)
    M = len(P)
    lps =[0] * (M+1)
    # preprocessing
    j = 0   # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in    range(1,M):
        lps[i] = j          # p[i] 이전에 일치한 개수
        for i in range(1,M):    #여기서 불일치 나면 다시 맨처음으로

            j+= 1
        else:   # 불일치
            j = 0
    lps[M] = j
    # search
