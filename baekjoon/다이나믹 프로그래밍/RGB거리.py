def fill_the_house(num_of_house):
    dp[1] = info[1] # 초기값

    for i in range(2, MAX):
        # dp[i][0] : i번째가 Red로 칠해졌을 때 최소 비용
        ## 즉, i-1번째가 Blue거나 Green인 경우에다가 i번째 Red의 비용을 합산한 값의 min을 계산하면 된다.
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + info[i][0] # i번째 집이 Red
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + info[i][1] # i번째 집이 Green
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + info[i][2] # i번째 집이 Blue

    return min(dp[num_of_house])

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_house = int(readline().strip())
    info = [[] for _ in range(num_of_house+1)]
    for idx in range(1, num_of_house+1):
        info[idx].extend(list(map(int, readline().split())))

    # dp 저장소를 만드는데, 모든 경우의 수를 커버하기 위해 n번째의 상황을 잘 해석해야 한다.
    ## n번째 집을 빨강, 초록, 파랑으로 칠했을 때 비용의 최솟값을 각각 저장하기 위해 인덱스를 나누었다.
    MAX = num_of_house + 1
    dp = [[0 for _ in range(3)] for _ in range(MAX)]

    print(fill_the_house(num_of_house))
