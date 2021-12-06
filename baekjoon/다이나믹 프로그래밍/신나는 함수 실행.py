def recursive_fn(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return recursive_fn(20,20,20)

    # memoization
    if dp[a][b][c]:
        return dp[a][b][c]

    # memo에 없으면 직접 계산
    else:
        if a < b < c:
            dp[a][b][c] = recursive_fn(a, b, c-1) + recursive_fn(a, b-1, c-1) - recursive_fn(a, b-1, c)
            return dp[a][b][c]

        dp[a][b][c] = recursive_fn(a-1, b, c) + recursive_fn(a-1, b-1, c) + recursive_fn(a-1, b, c-1) - recursive_fn(a-1, b-1, c-1)
        return dp[a][b][c]

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    MAX = 21
    dp = [[[0] * MAX for _ in range(MAX)] for _ in range(MAX)]
    while True:
        a, b, c = map(int, readline().split())
        if a == -1 and b == -1 and c == -1:
            break

        # 함수 실행
        result = recursive_fn(a,b,c)
        print(f"w({a}, {b}, {c}) = {result}")
