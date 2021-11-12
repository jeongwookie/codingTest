"""
BFS 혹은 DFS를 활용하여,
모든 노드에 대해서 상하좌우를 살피고 0이면 방문하고 1이면 방문하지 않음.
결국은 "방문 처리" 를 어떻게 기록할 것인가? 와
"방문 처리" 이후 어떻게 움직일 것인가? 두가지를 정의함이 핵심인 것 같다.
"""
# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
## 0의 값을 가진 노드를 방문하게 되면 해당 값을 1로 바꿔줌. 그리고 상하좌우 움직일 수 있게 함.
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우는 즉시 종료
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    # 현재 노드를 아직 방문하지 않은 경우 (첫 방문)
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리함
        graph[x][y] = 1
        # 해당 좌표를 기준으로 상하좌우로 재귀 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True # 첫 방문일때만 상하좌우 움직이고, True를 반환함

    # 원래 값이 1이거나, 위 과정으로 인해 재귀적으로 방문된 노드인 경우 False 반환
    return False

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split())

    # 2차원 리스트의 맵 정보 입력 받기
    graph = []
    for _ in range(N):
        graph.append(list(map(int, list(readline().strip()))))
    print(graph)

    # 모든 노드에 대하여 음료수 채우기
    result = 0
    for i in range(N):
        for j in range(M):
            # 현재 위치에서 dfs 수행
            ## 해당 노드가 True다 : 노드를 처음으로 방문했더니 값이 0이었다. 그리고 해당 노드의 상하좌우로 1이 나올때까지 재귀적으로 돌아다녔다.
            if dfs(i, j) == True:
                result += 1

    print(result) # 정답!