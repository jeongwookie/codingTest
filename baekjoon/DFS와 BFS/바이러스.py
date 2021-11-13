def dfs(graph, v, visited):
    # 해당 노드에 대해 방문 처리
    visited[v] = True
    # 인접 노드 탐색
    for i in graph.get(v):
        # 인접 노드가 방문된 적이 없다면, 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_computers = int(readline())
    num_of_linked_pairs = int(readline())
    graph = {k:[] for k in range(1, num_of_computers+1)} # initialize

    for _ in range(num_of_linked_pairs):
        c1, c2 = map(int, readline().split())
        # graph dict에 노드 관계 저장
        graph[c1].append(c2)
        graph[c2].append(c1)
    #print(graph)

    visited = [False] * (num_of_computers + 1) # 0번 인덱스는 무시
    dfs(graph, 1, visited) # 1번 컴퓨터에서 바이러스가 시작되었을 때, dfs 수행하기
    print(len([i for i in visited[1:] if i]) - 1) # 0번 인덱스는 빼고, 자기 자신도 빼고 True인 값만 세어서 리턴