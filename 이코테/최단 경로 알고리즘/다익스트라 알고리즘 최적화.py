if __name__ == "__main__":
    import heapq

    # 인풋 구성 : graph[a] = [b,c] a에서 b까지 가는 거리가 c
    graph = [
        [], # 노드 0번은 빈칸 처리
        [[2, 2], [3, 5], [4, 1]], # 노드 1번에서 2번까지 가는데 비용 2, 1번에서 3번까지 가는데 비용 5 등등
        [[3, 3], [4, 2]],
        [[2, 3], [6, 5]],
        [[3, 3], [5, 1]],
        [[3, 1], [6, 2]],
        [] # 노드 6번에서 나가는 간선이 없음
    ]

    # 저장소 설정
    INF = int(1e9)
    visited = [False for _ in range(len(graph))]
    distance = [INF for _ in range(len(graph))]
    start = 1  # 인풋으로 주어지는 start node

    # 다익스트라 알고리즘
    def dijkstra(start):

        # 초기 설정
        priority_queue = []
        distance[start] = 0 # 시작점에서의 최소 거리 비용은 0
        heapq.heappush(priority_queue, (distance[start], start)) # 힙에 (거리, 노드번호) 이렇게 넣어줌

        while priority_queue: # 큐가 비어있지 않다면
            curr_dist, curr_node = heapq.heappop(priority_queue) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            if visited[curr_node]: # 이미 방문한 노드라면
                continue
            else:
                visited[curr_node] = True # 현재 노드 방문 처리

            # 인접 노드 탐색
            for next_node, cost in graph[curr_node]:
                next_dist = curr_dist + cost
                # 방문한 노드가 아니고, 원래 저장되어 있는 값보다 거쳐갈 때 더 값이 작을 경우
                if not visited[next_node] and next_dist < distance[next_node]:
                    distance[next_node] = next_dist # 갱신
                    heapq.heappush(priority_queue, (distance[next_node], next_node)) # 갱신된 기준으로 넣어줌


    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(1, len(graph)):
        # 도달할 수 없는 경우
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])

