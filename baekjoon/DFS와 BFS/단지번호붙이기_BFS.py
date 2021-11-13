from collections import deque
"""
bfs 식 풀이는, 큐를 사용하며
큐에 넣는 순간 방문 처리를 수행함.
그리고 큐가 빌때까지 루프 돌리는데, 루프 안에서 방금 방문처리한 좌표 근처를 탐색하고,
탐색된 좌표들을 통째로 큐에 넣고 그 동시에 방문처리를 수행함.
"""
def bfs(x, y):
    count = 0
    if graph[x][y] == 0: # (x,y) 에 집이 없으면 False
        return count

    else: # (x,y) 에 집이 있는 경우 True
        # queue 생성 후 해당 좌표를 넣음
        queue = deque([(x,y)])
        graph[x][y] = 0  # 방문 처리
        count += 1

        # 해당 좌표를 기점으로 bfs를 수행하고, 방문 처리된 집을 count로 저장함
        while queue:
            v = queue.popleft() # 큐에서 이미 방문한 놈 제거함

            # v의 상하좌우를 탐색
            dx = [1, -1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                var_x = v[0] + dx[i]
                var_y = v[1] + dy[i]
                if var_x<0 or var_x>len(graph)-1 or var_y<0 or var_y>len(graph)-1: # 범위를 넘어갈 경우 탐색하지 않음.
                    continue
                # 집이 있는 경우만 탐색함
                if graph[var_x][var_y] != 0:
                    queue.append((var_x, var_y))  # 먼저 큐에 넣고,
                    graph[var_x][var_y] = 0  # 해당 좌표를 방문 처리함
                    count += 1

        return count

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline())
    graph = []
    for _ in range(N):
        read = list(readline().strip())
        graph.append(list(map(int, read)))

    num_of_house_group = 0
    num_of_house = []
    for i in range(N):
        for j in range(N):
            result = bfs(i, j)
            if result != 0: # 0이 아닌 경우, 최소 1집은 있다는 뜻임
                num_of_house.append(result)
                num_of_house_group += 1 # 단지 수 저장

    # 결과 출력
    print(num_of_house_group)
    [print(i) for i in sorted(num_of_house)] # 오름차순 정렬
