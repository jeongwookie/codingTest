"""
DFS와 BFS로 탐색한 결과를 출력하는 프로그램 작성
처음 인풋을 노드와 노드사이의 관계를 표현한 dict으로 변경하는 과정에서 누락이 생김.
정점과 정점을 이을 때, 하나의 선만 있는 게 아님. 여러 개가 존재할 수 있음.
"""
from collections import deque

def dfs(graph, V, visited):
    # 현재 노드를 방문 처리
    visited[V] = True
    print(V, end=' ') # 방문한 노드를 출력
    # 인근 노드를 재귀적으로 방문
    for i in graph[V]: # 인근 모든 노드에 대해서
        if not visited[i]: # 방문하지 않은 노드라면, dfs을 수행하라.
            dfs(graph, i, visited)


def bfs(graph, V, visited):
    # 큐 만들고, 해당 노드를 저장함
    ## 해당 노드를 방문 처리함
    queue = deque([V])
    visited[V] = True
    # 인근 노드를 탐색함
    while queue:
        curr_node = queue.popleft()
        print(curr_node, end=' ') # 방문한 노드를 출력
        for i in graph[curr_node]: # 인근 노드를 전부 탐색
            if not visited[i]: # 아직 방문하지 않은 노드라면, 전부 큐에 넣음
                queue.append(i)
                visited[i] = True # 큐에 넣은 노드에 대해서는 전부 방문 처리함


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M, V = map(int, readline().split()) # 정점 갯수, 간선 갯수, 탐색 시작 정점 번호
    input_graph = []
    for _ in range(M):
        input_graph.append(list(map(int, readline().split())))

    # 이거를 노드 관계의 그래프로 바꿔줌
    ## 어떤 두 정점 사이에 여러개의 간선이 있을 수 있다!! 는 조건을 간과함. "1 2" "1 2" 가 가능함.
    graph = {k:[] for k in range(1, N+1)} # 정점 번호를 key로 가진 dict
    for v1, v2 in input_graph:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # value 정렬
    graph = {k:sorted(v) for k,v in graph.items()}
    print(graph)

    # dfs 수행
    visited = [False] * (N+1) # 0번 인덱스는 신경쓰지 않기 위해 1을 추가함
    dfs(graph, V, visited)
    print()

    # bfs 수행
    visited = [False] * (N+1)
    bfs(graph, V, visited)

