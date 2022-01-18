if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split()) # M(target) : 15
    array = []
    for _ in range(N): # N가지 종류의 화폐 입력. 예시에서는 2와 3 받음
        array.append(int(readline()))

    """
    dp[i] : 금액 i를 만들 수 있는 최소한의 화폐 갯수
    k : 각 화폐의 단위 (2,3,7,...)
    점화식 :
        dp[i-k]를 만드는 방법이 존재하는 경우 => dp[i] = min(dp[i], dp[i-k]+1)
        dp[i-k]를 만드는 방법이 존재하지 않는 경우 => dp[i] = INFINITE
    이때, INFINITE값을 "문제에서 만들 수 없는 값"으로 넣어놓으면 된다.
    현재 문제 조건을 보면 target인 M의 범위가 10000까지 이므로, 문제의 조건에서 벗어난 10001 이라는 값을 사용한다.
    """
    INF = 10001
    dp = [INF for _ in range(M+1)] # 최대 금액 M까지 저장할 수 있는 dp table. 전부 만들 수 없다고 가정
    dp[0] = 0 # 0원은 필요한 화폐가 없음

    for i in range(N): # 각 화폐 단위에 대한 인덱스
        coin_unit = array[i]
        for j in range(coin_unit, M + 1): # Target을 늘려감.. M까지
            if dp[j - coin_unit] != INF: # 금액 i-coin_unit를 만들수 있는지 확인
                dp[j] = min(dp[j], dp[j - coin_unit] + 1)

    # 결과 출력
    if dp[M] == INF:
        print(-1)
    else:
        print(dp[M])



