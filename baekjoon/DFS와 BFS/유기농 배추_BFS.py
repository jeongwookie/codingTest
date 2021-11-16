def find_near_cabage(i, j):
    """
    point(i,j) 에서 시작해서 BFS로 인접 땅을 검사하여 배추가 있는 곳을 찾는다.
    이미 방문한 땅은 1에서 0으로 값을 바꾼다.
    해당 시작점에 배추가 있다면 True를, 없으면 False를 return한다.
    탐색이 범위를 넘어가게 되면 False를 return한다.
    """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    if validate_point(i, j): # 배추가 있는 경우
        queue = deque([(i, j)]) # 현재 포인트를 큐에 저장
        graph[i][j] = 0 # 방문 처리: 1을 0으로 바꿈

        while queue:
            x, y = queue.popleft()
            for idx in range(4): # 상 하 좌 우 인접한 포인트 탐색
                near_x, near_y = x + dx[idx], y + dy[idx]
                if validate_point(near_x, near_y): # near_x, near_y가 유효한 범위이면서 배추가 있는 경우,
                    queue.append((near_x, near_y)) # 모두 큐에 넣고
                    graph[near_x][near_y] = 0 # 방문 처리

        return True

    else:
        return False

def validate_point(x,y):
    """
    (x,y)에 배추가 있고 범위를 넘어가지 않는 경우 True를 리턴
    배추가 없거나, 범위를 넘어가는 경우 전부 False를 리턴
    """
    if x<0 or x>length-1 or y<0 or y>width-1: # 범위를 넘어가는 경우
        return False

    if graph[x][y] == 0:
        return False

    else:
        return True

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000)
    from collections import deque
    num_of_test_case = int(readline().strip()) # test case 갯수

    for _ in range(num_of_test_case):
        width, length, num_of_cabbage = map(int, readline().split())
        graph = [[0 for _ in range(width)] for _ in range(length)] # 0으로 초기화

        for _ in range(num_of_cabbage):
            x, y = map(int, readline().split()) # 배추의 위치 좌표를 입력받음.
            graph[y][x] = 1 # 배추가 있는 위치를 1로 표기, x와 y를 반대로 입력받음.

        # 배추 탐색 수행
        count = 0 # 필요한 배추흰지렁이의 갯수
        for i in range(length):
            for j in range(width):
                if find_near_cabage(i, j): # 배추가 있는 땅이면 지렁이 갯수 1 늘려주기
                    count += 1
        print(count)
