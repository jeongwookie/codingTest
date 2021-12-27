if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    array = list(map(int, readline().split()))

    # 연속된 수만 선택 가능
    # dp[i] : array i번째 수를 마지막으로 가지는 부분합 중 max값을 저장
    dp = [0 for _ in range(N)]
    dp[0] = array[0]

    # 그냥 dp[8]과 dp[7]을 다 적어보니 결과가 이런식으로 나옴
    # 예시 1번에 대해서, 푸는 방법을 그냥 적다보니까 점화식이 간단하게 나옴
    for i in range(1, N):
        dp[i] = max(array[i], array[i] + dp[i-1])

    print(max(dp))


