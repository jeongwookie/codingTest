def calculate_min_count(i, j):
    """
    start 지점 (0,0)에서 시작해서 end 지점인 (N-1, M-1) 까지 이동하는데 최소한으로 움직여야함.
    최소한의 칸으로 움직였을 때 해당 칸 갯수를 세어서 리턴함.
    언제 최소한의 칸으로 움직이는거지? 방향을 제어하기엔 어려운 것 같음.
    Brute force 식으로 다 세봐야 할거같은데..? 어떻게 세야하나? 루트의 갯수가 얼마인지도 알 수 없는데.
    -> 최소한의 칸으로 움직이는 경우의 수를 세는 것 자체가 bfs를 진행한 것이다..!!
    """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    # BFS
    queue = deque([(i,j)])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        # 최종 경로에 도착했다면,
        if x == end[0] and y == end[1]:
            print(visited[x][y])
            break

        # 인접 탐색
        for idx in range(4):
            next_x, next_y = x + dx[idx], y + dy[idx]
            if 0 <= next_x < N and 0 <= next_y < M : # 유효한 포인트라면,
                if visited[next_x][next_y] == 0 and graph[next_x][next_y] == 1: # 한번도 방문하지 않았고, 길이 있다면
                    visited[next_x][next_y] = visited[x][y] + 1
                    queue.append((next_x, next_y))


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000)
    from collections import deque
    N, M = map(int, readline().split())
    graph = []
    for _ in range(N):
        input = readline().strip()
        graph.append([int(i) for i in input])

    # (0, 0) 에서 -> (N-1, M-1)으로 가는 최소의 칸 수
    end = (N-1, M-1)
    calculate_min_count(0, 0)
