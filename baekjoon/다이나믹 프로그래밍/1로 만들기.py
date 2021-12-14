if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    dp = [0] * (N+1)

    # 초기값 정의 : 0과 1은 그대로 둬도 된다 둘다 0임

    ## 어떤 수 N이 있을 때 연산가능한 경우를 점화식으로 표현하면 되겠다..!!
    for i in range(2, N+1):
        candidate = [] # 아래 3개의 식에서 최소값을 찾아서 실제 dp[i]로 할당해야함.
        #1. 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            candidate.append(dp[i // 3] + 1)
        #2. 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            candidate.append(dp[i // 2] + 1)
        #3. 아무것도 아닌 경우
        candidate.append(dp[i - 1] + 1)
        dp[i] = min(candidate)

    print(dp[N])
