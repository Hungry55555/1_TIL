graph = [
    [0,1,0,1,0],   
    [1,0,1,0,1], 
    [0,1,0,0,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
]

# 갈수 있는 곳 다 가기
# 방문 순서대로 다음 노드

def bfs(start):
    visited=[0]*5

    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now,end=' ')

        # 갈 수 있는 곳을 체크
        for to in range(5):
            if graph[now][to] == 0:
                continue
            
            if visited[to]:
                continue
        
            visited[to] = 1
            print(visited)
            queue.append(to)

bfs(0)