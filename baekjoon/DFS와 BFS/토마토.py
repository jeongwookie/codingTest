def ripen_tomatoes(start_points):
    queue = deque(start_points) # 무조건 토마토가 있는 좌표가 들어옴
    while queue:
        x, y = queue.popleft()
        # 주변 탐색
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]

        for idx in range(4):
            next_x, next_y = x + dx[idx], y + dy[idx]
            if valid_point(next_x, next_y):
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1 # 방문 처리


def valid_point(x, y):
    """
    (x,y)가 주어진 범위를 넘어가면 False,
    해당 좌표에 0이 있어야 첫 방문으로, True 리턴. -1이 있으면 방문할 수 없음 False 리턴
    이미 익은 토마토를 또 방문하는건 괜찮은가? 괜찮긴 한데 굳이 그럴 필요가 없네.
    """
    if x < 0 or x > length-1 or y < 0 or y > width-1:
        return False
    if graph[x][y] != 0:
        return False
    else:
        return True

def find_first_tomatos():
    """
    시작 가능한 포인트 : 1이 있는 곳
    """
    start_points = []
    for i in range(length):
        for j in range(width):
            if graph[i][j] == 1:
                start_points.append((i, j))
    return start_points

def is_well_done():
    for i in range(length):
        for j in range(width):
            if graph[i][j] == 0: # 안익은 토마토가 있다면?
                return False
    return True

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000)
    from collections import deque

    width, length = map(int, readline().split())
    graph = []
    # input 정리
    for _ in range(length):
        graph.append(list(map(int, readline().split())))

    start_points = find_first_tomatos() # 시작점으로 가능한 포인트들을 찾기 : 1이 있는 경우
    ripen_tomatoes(start_points) # 토마토 익히기

    # 모든 토마토가 익었는가?
    if is_well_done():
        print(max([max(i) for i in graph]) - 1)
    else:
        print(-1) # 안익음


