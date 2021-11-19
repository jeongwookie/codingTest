def bfs():
    queue = deque([[0,0,0]]) # 시작점, 마지막 원소는 break_wall_count
    while queue:
        x, y, break_wall_count = queue.popleft()
        visited[x][y] = True

        # 최종 도착지점 설정
        if x == N-1 and y == M-1:
            print(graph[x][y] + 1) # 제일 첫칸 더해줌
            break

        # 움직임 정의
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for idx in range(4):
            next_x, next_y = x + dx[idx], y + dy[idx]
            if 0<=next_x<N and 0<=next_y<M: # 범위 내에 존재하는지 체크

                # 이동할 수 있는 경우
                if graph[next_x][next_y] == 0 and visited[next_x][next_y] == False:
                    visited[next_x][next_y] = True # 방문 처리
                    graph[next_x][next_y] = graph[x][y] + 1 # 움직인 칸 수 누적
                    queue.append([next_x, next_y, break_wall_count])

                # 벽인 경우 + non-visited인 경우 => 방문하되 벽을 뚫은 count를 기록함
                ## break_wall_count가 1이 넘어가면 아예 방문하지 않음.
                ## 문제가 있는데, 지금 이대로 하면 처음 만난 1을 무조건 뚫어보고 생각한다는거임;;;;; 이러면 오류가 생김.
                ### 여기서 기록하는 graph 자체의 분기를 나누고 싶은데 .... 너무 복잡하네.
                elif graph[next_x][next_y] == 1 and visited[next_x][next_y] == False and break_wall_count == 0:
                    # 이걸 뚫을꺼냐? 말꺼냐? 를 정해야함. 근데 정할 근거가 나중에 있어서.. brute force로 다 세주는 방법이 맞지않나?
                    # 으악!!! 해당 벽을 뚫은 경우가 더 최단거리인지, 안뚫고 이따 나중에 만난 벽을 뚫는게 더 최단거리인지 현 시점에서는 알 방법이 없음.
                    visited[next_x][next_y] = True  # 방문 처리
                    graph[next_x][next_y] = graph[x][y] + 1 # 움직인 칸 수 누적
                    queue.append([next_x, next_y, break_wall_count + 1]) # 벽을 뚫은 count를 누적


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

    visited = [[False for _ in range(M)] for _ in range(N)]
    # (1,1)부터 (N,M)까지 -> (0,0)부터 (N-1,M-1)까지로 처리
    ## bfs로 최단거리 수행
    # graph의 차원을 늘려서 벽 만나면 분기를 나눠서 하고싶은데, 너무 복잡하다 ㅠ
    bfs()

    print(graph)