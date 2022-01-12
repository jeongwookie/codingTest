def dfs(depth, idx):
    global minimum
    if depth == N//2: # 한 팀의 모집이 완료된 경우,
        team_1, team_2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 방문한 노드가 모인 팀
                    team_1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    team_2 += graph[i][j]

        minimum = min(abs(team_1 - team_2), minimum)
        return

    for i in range(idx, N):
        if not visited[i]: # 방문하지 않은 노드이면,
            visited[i] = 1 # 방문 처리
            dfs(depth+1, i+1) # dfs로 다음 노드 진행하되 idx를 다음으로 넘겨버린다.
            visited[i] = 0 # backtracking : revert


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, readline().split())))

    visited = [0 for _ in range(N)]
    minimum = 1e9
    dfs(0, 0)
    print(minimum)
