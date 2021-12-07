"""
프렉탈 비슷한 문제들은 딴게 없다.
그냥 뭔가 규칙성을 발견할때까지 하나씩 적어보면 된다.
p(1)부터 p(11)쯤까지 쭉 따라가면서 써보니까 점화식이 보였다.
그대로 써주고 bottom-up 방식으로 풀이하면 끝.
"""

def p_sequence(N):
    if dp[N]:
        return dp[N]

    for i in range(6, N+1):
        dp[i] = dp[i-1] + dp[i-5]

    return dp[N]

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    T = int(readline().strip())
    MAX = 100
    dp = [0] * (MAX + 1)

    # 초기값 세팅
    dp[1], dp[2], dp[3] = 1, 1, 1
    dp[4], dp[5] = 2, 2

    for _ in range(T):
        print(p_sequence(int(readline().strip())))