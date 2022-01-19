def max_gold():
    result = 0

    # 초기값 채워주기
    for i in range(n):
        dp[i][0] = graph[i][0]

    # loop의 순서가 내가 생각한 것과 다르다..!!
    ## y(열)을 한칸씩 이동시키면서 계산을 해야하기 때문에 for문 가장 바깥을 열로 두어야 제대로 된 결과가 나옴.
    for y in range(1, m):
        for x in range(n):
            if x == 0:
                x_left_up = 0
            else:
                x_left_up = dp[x-1][y-1]

            if x == n-1:
                x_left_down = 0
            else:
                x_left_down = dp[x+1][y-1]

            dp[x][y] = max(dp[x][y-1], x_left_up, x_left_down) + graph[x][y]

            # 마지막 열에 도달했을 때 값을 갱신함
            if y == m-1:
                result = max(result, dp[x][y])
    print(dp)
    return result


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    test_case = int(readline().strip())
    for _ in range(test_case):
        n, m = map(int, readline().split())
        array = list(map(int, readline().split()))
        graph = []
        itr = 0
        for i in range(n):
            graph.append(array[itr:itr+m])
            itr += m

        # answer
        dp = [[0] * m for _ in range(n)]
        print(max_gold())
