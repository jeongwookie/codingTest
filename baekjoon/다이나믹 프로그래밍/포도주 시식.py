if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    wine_array = [0]
    for _ in range(N):
        wine_array.append(int(readline().strip()))

    """
    i번째 포도주를 마시지 않는 경우 : i-1번째 max값과 동일한 값임
    i번째 포도주를 마시는 경우 : i-1번째 포도주를 마시는 경우 / 마시지 않는 경우를 잘 판단해야함.
    (연속)
    i-1번째 포도주를 마시는 경우 : i-2번째 포도주는 반드시 마시면 안됨
    i-1번째 포도주를 마시지 않는 경우 : 그냥 dp[i-1][0]의 모든 경우의 수
    
    dp를 저장할 때 i번째에서 포도주 안마신 경우 0번, 마신 경우 1번 인덱스로.
    """

    dp = [[0] * 2 for _ in range(N+1)]
    dp[1][0], dp[1][1] = 0, wine_array[1]

    for i in range(2, N+1):
        # i 번째 포도주를 마시지 않은 경우
        dp[i][0] = max(dp[i-1])

        # i 번째 포도주를 마신 경우
        ## i-1 번째 포도주를 마신 경우와 안마신 경우를 모두 고려해야함
        no_wine_before_ith = dp[i-1][0]
        yes_wine_before_ith = dp[i-2][0] + wine_array[i-1] # i-1 번째 포도주를 마신 경우, i-2번째는 무조건 마시면 안됨
        dp[i][1] = wine_array[i] + max(no_wine_before_ith, yes_wine_before_ith)

    print(max(dp[N]))


