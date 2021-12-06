def solution(n):
    # dp[1]인 경우는 0이므로 이미 초기화 되어있는 셈이다.
    # dp[1] = 0

    # bottom-up 방식으로 탐색
    for i in range(2, n+1):
        candidate = []
        if i % 5 == 0:
            candidate.append(dp[i//5] + 1)
        if i % 3 == 0:
            candidate.append(dp[i//3] + 1)
        if i % 2 == 0:
            candidate.append(dp[i//2] + 1)

        candidate.append(dp[i-1] + 1)
        dp[i] = min(candidate)

    return dp[n]

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    X = int(readline().strip())
    MAX = 30000 + 1
    dp = [0] * MAX
    print(solution(X))
