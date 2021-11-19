"""
항상 기억하자. bfs는 queue에 넣고 곧바로 방문처리한다. 이후 while문이다.
while문 안에서도 queue에 넣고 곧바로 방문처리가 기본이다.
어려운 문제임. 핵심 포인트를 꼽자면,
1. visited를 한 차원 올려서 두가지 케이스에 대해서 모두 저장 -> 지금까지 한번도 벽 뚫은 적이 없는 경우의 수, 벽 한번 뚫고 온 경우의 수
2. bfs를 위해 queue에 인접 방문 좌표를 append해줄때, 인접 방문 시 벽을 뚫었는지 안뚫었는지까지 전달해주어야함 -> 역시 차원을 올려서 전달
"""

def bfs():
    queue = deque([[0,0,0]]) # 마지막 원소 : 지금까지 wall을 뚫은적이 있으면 1 없으면 0
    visited[0][0][0] = 1  # 시작점은 wall이 무조건 없음
    while queue:
        x, y, wall = queue.popleft()

        # 최종 도착지점 설정
        if x == N-1 and y == M-1:
            print(visited[x][y][wall])
            break

        # 움직임 정의
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for idx in range(4):
            next_x, next_y = x + dx[idx], y + dy[idx]
            if 0<=next_x<N and 0<=next_y<M: # 범위 내에 존재하는지 체크

                # 한번도 방문한 적이 없는 좌표에 대해서 체크 -> wall을 넘겨줌으로써 그전 상태가 어떤지 알 수 있음.
                ## wall이 0일수도 1일수도 있다는 의미.
                ## 벽을 방문하고, 이후에 인접한 노드를 방문하여도 인덱스 1번에만 값이 누적되어 저장되기 때문에,
                ## 바로직전에 벽을 방문하지 않은 노드가 이후에 인접한 노드를 방문할 경우, 인덱스 0번은 그대로 초기값 0이기에 방문이 가능하다!
                if visited[next_x][next_y][wall] == 0:
                    # 벽이 아닌 경우 -> 정상적으로 이동. 그 전 wall값을 보고 해당 자리에 값을 저장
                    if graph[next_x][next_y] == 0:
                        queue.append([next_x, next_y, wall])
                        visited[next_x][next_y][wall] = visited[x][y][wall] + 1 # 방문처리 : visited에 값 누적

                    # 벽인 경우, 벽을 한번도 부수지 않았어야함. wall의 값이 0으로 잡혀있어야함.
                    if wall == 0 and graph[next_x][next_y] == 1:
                        queue.append([next_x, next_y, 1])  # queue에 좌표 넣을때 벽을 뚫었음을 표시함.
                        visited[next_x][next_y][1] = visited[x][y][wall] + 1  # 방문 처리 : visited 중 wall 뚫은 1번자리에 값 누적

    # 지점들을 모두 선회했는데 if문에 걸리지 않은 경우, -1
    ## 최종 지점 (N-1, M-1)에 도달하지 않았다..!!
    if x != N-1 or y != M-1:
        print(-1)


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000)
    from collections import deque
    N, M = map(int, readline().split())
    graph = []
    for i in range(N):
        graph.append([int(s) for s in readline().strip()])

    # visited 원소 [0,0] : (벽을 뚫지 않고 온 경우 최단 경로 갯수, 벽을 1번만 뚫고 온 경우에 대한 최단 경로 갯수)
    visited = [[[0,0] for _ in range(M)] for _ in range(N)]

    # (1,1)부터 (N,M)까지 -> (0,0)부터 (N-1,M-1)까지로 처리
    ## bfs로 최단거리 수행
    ### graph에 직접 값을 업데이트 하는게 아니라, visited에다가 값 올리고 graph는 계속 가만히 놔둠
    bfs()
