from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = list(map(int, input().split()))
map_ = []
for _ in range(N):
    map_.append(list(input()))

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[[] for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if map_[i][j] == '1':
            continue 
        if i-1>-1 and map_[i-1][j] == '0':
            graph[i][j].append((i-1, j))
        if i+1<N and map_[i+1][j] == '0':
            graph[i][j].append((i+1, j))
        if j-1>-1 and map_[i][j-1] == '0':
            graph[i][j].append((i, j-1))
        if j+1<M and map_[i][j+1] == '0':
            graph[i][j].append((i, j+1))

print(graph)