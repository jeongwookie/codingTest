"""
n번째 상황을 생각해보면,
n-1번째에다가 1을 붙이거나, n-2번째에다가 00을 붙이는 두가지 경우 뿐이다.
피보나치와 같은 점화식
"""

def available_sequence(N):
    dp[1], dp[2] = 1, 2

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 메모리 초과 때문에 여기서 나눠서 저장해줘야함.

    return dp[N]

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    MAX = 1000000 + 1
    dp = [0] * MAX
    print(available_sequence(N))
