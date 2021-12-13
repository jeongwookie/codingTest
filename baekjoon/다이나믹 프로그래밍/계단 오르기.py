def max_score(stairs):
    if len(stairs) == 1:
        return stairs[0]
    elif len(stairs) == 2:
        return stairs[1] + stairs[0]
    else:
        # 초기값
        dp[0][0], dp[0][1] = stairs[0], stairs[0]
        dp[1][0], dp[1][1] = stairs[1], stairs[1] + stairs[0]

        # loop
        for i in range(2, num_of_stairs):
            dp[i][0] = stairs[i] + max(dp[i - 2][0], dp[i - 2][1])  # 0번 인덱스이므로, i번째 칸 밟고 i-2번째 칸 밟는 경우를 계산
            dp[i][1] = stairs[i] + dp[i - 1][0]  # 1번 인덱스이므로, i번째 칸 밟고 i-1번째 칸 밟는 경우를 계산

        # 결과 출력 : status 2개 중 max값을 리턴하면 종료
        return max(dp[num_of_stairs - 1])


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_stairs = int(readline().strip())
    stairs = []
    for _ in range(num_of_stairs):
        stairs.append(int(readline().strip()))

    # dp에 status 2개를 저장함
    ## 인덱스 0번에는 두칸앞을 밟은 경우, 1번에는 한칸앞을 밟은 경우를 저장함
    dp = [[0] * 2 for _ in range(num_of_stairs)]
    print(max_score(stairs))