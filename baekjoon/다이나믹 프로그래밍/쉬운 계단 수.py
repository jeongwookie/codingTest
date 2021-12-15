if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())

    # 길이가 N인 계단수의 갯수 세기
    MAX = 100 + 1
    dp = [[0 for _ in range(10)] for _ in range(MAX)]

    # 초기값, N=0은 존재할 수 없으므로 무시함
    # dp[1] : N이 1일때 각각의 상황을 저장
    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 0~9로 끝나는 계단수의 갯수 저장

    for level in range(2, N+1):
        for i in range(0, 10):
            # n level 에서 0으로 끝나는 경우 : n-1 level에서 1로 끝나야지만 뒤에 0을 붙일 수 있음
            if i == 0:
                dp[level][i] = dp[level-1][i+1]
            # n level 에서 9로 끝나는 경우 : 마찬가지로 직전에 8로 끝나야 가능함
            elif i == 9:
                dp[level][i] = dp[level-1][i-1]
            # 나머지 1부터 8까지는 각각 두가지 케이스가 존재함 (up, down)
            else:
                dp[level][i] = dp[level-1][i-1] + dp[level-1][i+1]

    # 결과 출력
    print(sum(dp[N]) % 1000000000)
