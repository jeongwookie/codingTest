if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    n, m = map(int, readline().split()) # 노드의 갯수, 간선의 갯수
    start = int(readline().strip()) # 시작 노드 번호 입력

    # 간선 정보 입력
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, readline().split())
        graph[a].append([b, c]) # 노드 a에서 출발해 노드 b까지 가는 비용이 c

    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
    visited = [False] * (n+1) # 방문 체크 목적의 리스트
    distance = [INF] * (n+1) # 최단 거리 갱신하는 테이블. 각 인덱스 노드에 도착하는 최단 거리를 저장함.

    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    def get_smallest_node():
        min_value = INF
        index = 0 # 가장 최단 거리가 짧은 노드 번호
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]: # 루프 다 돌면서 최소값 비교. 방문하지 않은 노드만!
                min_value = distance[i]
                index = i

        return index

    # 다익스트라 알고리즘
    def dijkstra(start):
        # 시작 노드에 대해서 초기화
        distance[start] = 0
        visited[start] = True
        for next_node, cost in graph[start]: # 시작 노드와 인접한 모든 노드들에 대해서
            distance[next_node] = cost # 해당 노드로 가는 최소 비용을 갱신

        # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
        for i in range(n-1):
            # 현재 최단 거리 갱신 테이블 안에서, 가장 작은 값을 가진 노드를 꺼내서 방문 (greedy algorithm)
            now = get_smallest_node()
            visited[now] = True
            # 현재 방문 중인 노드와 연결된 다른 노드를 확인함
            for next_node, cost in graph[now]:
                next_visit_node_cost = distance[now] + cost
                # 방금 계산한 cost 가 기존에 저장되어 있던 cost 보다 작을 경우 갱신
                if next_visit_node_cost < distance[next_node]:
                    distance[next_node] = next_visit_node_cost

    # 다익스트라 수행
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(1, n+1):
        # 도달할 수 없는 경우
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
