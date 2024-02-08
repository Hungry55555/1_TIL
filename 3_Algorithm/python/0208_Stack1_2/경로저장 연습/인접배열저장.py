# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 주로 인풋은 간선( E), 정점(V) 정보를 같이 줌
# 인접 배열을 저장할 때는 간선의 정보를 이용해서 저장하면 됨
# 인접 배열을 초기화할때는 정점정보를 이용하면 됨
V,E = 7,8   # map(int,input().split())
edge_list = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# w정점의 개수만틈 2차원 리스트로 만들면 됨
# 0은 연결되어있지 않음을 의미
# 정점의 번호를 그대로 저장하기 위해 +1을 함
# 즉 정점의 갯수와 정점의 인덱스를 생각하면 플러스 왜하는지 이해가 된다.

adj_arr = [[0]*(V+1) for _ in range(V+1)]   

for idx in range(E):
    # 시작점(idx*2), 돡점(idx*2+1)
    start = edge_list[idx*2]
    end = edge_list[idx*2  + 1]
    # 인접 배열 저장
    adj_arr[start][end]=1 
    # 만약 양방향으로 저장해야 한다면
    # add_arr[end][start] = 1

for v in range(V+1):
    print(*adj_arr[v])