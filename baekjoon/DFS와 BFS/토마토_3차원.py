def ripen_tomatos_bfs(start_point):
    queue = deque(start_point)
    max_val = 0
    while queue:
        z,x,y = queue.popleft()
        # 인접 기준 설정 (상 하 좌 우 위 아래)
        dx = [-1,1,0,0,0,0]
        dy = [0,0,-1,1,0,0]
        dz = [0,0,0,0,1,-1]
        for idx in range(6):
            next_x, next_y, next_z = x + dx[idx], y + dy[idx], z + dz[idx]
            if valid_point(next_z, next_x, next_y): # 해당 포인트가 유효한 포인트라면,
                graph[next_z][next_x][next_y] = graph[z][x][y] + 1 # 방문처리
                queue.append([next_z, next_x, next_y])
                if graph[next_z][next_x][next_y] > max_val: # max day 계산용 저장소
                    max_val = graph[next_z][next_x][next_y]

    if max_val != 0:
        return max_val - 1 # 정상적으로 진행되었다면 하루를 가산한 상태로 계산되므로 최종적으로 1을 빼줌
    else: # 모든 토마토가 이미 익어있는 경우,
        return max_val # 0

def valid_point(z,x,y):
    # 범위를 벗어나는 경우 false
    if x<0 or x>N-1 or y<0 or y>M-1 or z<0 or z>H-1:
        return False

    # 처음 방문하는 경우만 True
    if graph[z][x][y] == 0:
        return True
    else:
        return False # 1이상의 값이거나, -1인 경우가 해당됨.

def is_well_done():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] == 0:
                    return False
    return True

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000)
    from collections import deque

    M, N, H = map(int, readline().split()) # 가로, 세로, 높이
    graph = []
    start_point = []
    for h in range(H): # 높이 기준
        _list = []
        for n in range(N): # 세로 기준
            arg_list = list(map(int, readline().split()))
            # 토마토가 있는 경우 해당 좌표를 저장
            for m in range(M):
                if arg_list[m] == 1:
                    start_point.append([h,n,m])
            _list.append(arg_list)
        graph.append(_list)
    #print(graph) # 인덱싱 : graph[높이][세로][가로] 순서

    # 여섯방향에 있는 토마토들을 익힘
    ## 한 노드에 인접한 노드들을 모두 탐색하고, 최소 일수에 대해서 리턴 -> BFS
    max_ripen_days = ripen_tomatos_bfs(start_point)

    # graph에 하나라도 0이 포함되어 있으면 -1을 리턴해야함.
    # 그렇지 않으면 bfs 후 저장한 max값을 리턴
    if is_well_done():
        print(max_ripen_days)
    else:
        print(-1)



