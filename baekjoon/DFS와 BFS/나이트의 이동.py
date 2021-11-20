def bfs(start, end):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()

        # 도착
        if x == end[0] and y == end[1]:
            print(graph[x][y])
            break

        # 인접 탐색 (8방향)
        dx = [1,2,2,1,-1,-2,-2,-1]
        dy = [-2,-1,1,2,-2,-1,1,2]
        for idx in range(8):
            next_x = x + dx[idx]
            next_y = y + dy[idx]
            # 범위를 벗어나지 않는가?
            if 0<=next_x<size_of_board and 0<=next_y<size_of_board:
                # 방문한 적이 없는가? -> 따로 visited를 기록할 필요없이 graph에 바로 적음
                if graph[next_x][next_y] == 0:
                    queue.append([next_x, next_y])
                    graph[next_x][next_y] = graph[x][y] + 1 # 방문 처리


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000)
    from collections import deque
    num_of_test_case = int(readline().strip())
    for _ in range(num_of_test_case):
        # each test case
        size_of_board = int(readline().strip())
        graph = [[0 for _ in range(size_of_board)] for _ in range(size_of_board)]
        start = list(map(int, readline().split()))
        end = list(map(int, readline().split()))
        # bfs로 최소 이동 횟수를 탐색
        bfs(start, end)
