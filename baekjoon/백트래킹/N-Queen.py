def dfs(i): # i는 row를 의미
    global count
    if i == N: # row가 0부터 시작해서 N-1까지 다 채워진 후 딱 넘어가면 N임
        count += 1

    # 각 row에 퀸 놓기 : row당 퀸은 하나씩만 할당할 것임
    else:
        for j in range(N):
            row[i] = j # i번째 row에 j번 인덱스 위치에 퀸을 놓음 (i,j)
            if adjacent(i): # 위에서 지정한 Q 위치 (i,j)가 올바른가? i번째 row가 잘 놓아졌는가?
                dfs(i + 1) # row를 1 증가 시킴


# 열이 동일한 케이스와 대각선 케이스 두가지를 검사함
# i번째 row까지 내려온 상황
def adjacent(i):
    # 0번째 row부터 i-1번째 row까지
    for j in range(i):
        # row[x] : i번째 row에서 Q의 위치 (열)
        # row[i] : i보다 위쪽 row에서 Q의 위치 (열)
        # row[i] == row[j] : Q가 같은 열에 있으면 -> False -> 백트래킹
        # abs(row[i] - row[j]) == i - j : 열 - 열 = 행 - 행 이면 같은 대각선상에 있음!! -> 백트래킹
        if row[i] == row[j] or abs(row[i] - row[j]) == i - j:
            return False

    # i 이전의 모든 row에 대해서 Q위치가 올바른 경우, True를 반환하여 다음 단계로 넘어갈 수 있게 함
    # 즉, i번째 row의 Q 위치를 (i,j)로 픽스하는 것
    return True


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())

    # N-Queen
    row = [0] * N # ex. [1,3,0,2]면 첫번째줄 1번 자리에 Q가 있고, 두번째줄 3번 자리에 Q가 있고 등등 이다.
    count = 0
    dfs(0)

    # print out
    print(count)