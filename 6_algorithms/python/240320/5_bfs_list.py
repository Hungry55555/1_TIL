# 인접 리스트 BFS: 재귀
graph = [
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
]
# 갈수 있는 곳 다 가기
# 방문 순서대로 다음 노드
visited = [0]*5
def bfs(start):
    visited[start]=1

    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now,end=' ')

        # 갈 수 있는 곳을 체크
        for to in graph[now]:
            
            if visited[to]:
                continue
        
            visited[to] = 1
            # print(visited)
            queue.append(to)

bfs(0)