def row_check(row_idx, x):
    if x in graph[row_idx]:
        return False
    return True


def col_check(col_idx, x):
    _list = []
    for i in range(N):
        _list.append(graph[i][col_idx])
    if x in _list:
        return False
    return True


def square_check(row_idx, col_idx, x):
    row_start = (row_idx // 3) * 3
    col_start = (col_idx // 3) * 3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if x == graph[i][j]:
                return False
    return True


def dfs(i):
    if i == len(empty):
        # 최종 형태의 스도쿠 출력
        for row in graph:
            for v in row:
                print(v, end=' ')
            print()
        return

    # 빈칸에 숫자 채워넣기
    for x in range(1, 10):
        row_idx, col_idx = empty[i][0], empty[i][1]
        if row_check(row_idx, x) and col_check(col_idx, x) and square_check(row_idx, col_idx, x):
            graph[row_idx][col_idx] = x # 1~9 사이의 숫자를 성공적으로 할당
            dfs(i+1) # 다음 빈칸으로 이동
            graph[row_idx][col_idx] = 0 # revert


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    graph = []
    for _ in range(9):
        graph.append(list(map(int, readline().split())))

    # 스도쿠 규칙에 맞게 풀이.
    # 0 인 지점에 숫자를 채워넣어야 함.
    # 0 인 지점을 처음에 다 센다음 해당 갯수에 도달하면 종료

    N = 9  # 스도쿠 판 크기
    empty = [(i, j) for i in range(N) for j in range(N) if graph[i][j] == 0]
    dfs(0)
