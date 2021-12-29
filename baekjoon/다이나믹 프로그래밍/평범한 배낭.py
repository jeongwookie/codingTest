"""
https://velog.io/@himi/%EB%B0%B1%EC%A4%80-12865.-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD
해당 풀이를 참고함
"""
if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, K = map(int, readline().split())
    info = []
    for _ in range(N):
        info.append(list(map(int, readline().split())))

    # dp[i][j] : 첫번째부터 i번째까지 담을수 있고, 가방의 최대 무게가 j인 경우 최대 value를 저장
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1): # 가방에 담을 수 있는 물건을 하나씩 늘림
        weight, value = info[i-1]
        for j in range(1, K+1): # 최대 무게를 1부터 원래 최대값인 K까지 늘림
            if weight <= j: # 현재 무게가 가방안에 들어갈 경우, 가방에 넣을수도 안넣을수도 있다.
                # 현재 weight를 가방 안에 넣을 경우 : 나머지는 j - weight 의 무게만 가질 수 있음
                ## dp[i-1][j-weight] + value (현재 이 물건의 무게는 weight) => 총 무게를 j가 되도록 맞춰줌
                dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])

            else: # 가방 안에 안들어갈 경우, 무조건 못넣는다.
                ## 이 물건을 안담고, 이전 물건까지 담았을 때의 최고 가치를 저장
                dp[i][j] = dp[i-1][j]

    print(dp[N][K])