"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
1. N에서 1을 뺀다
2. N을 K로 나눈다 : 해당 연산은 N이 K로 나누어떨어질 때만 수행한다.

예) N이 17일때, 1을 빼고 4로 나눈걸 두번하면 1이된다. 전체 수행 횟수는 3
N이 1이 될때까지 과정을 수행해야 하는 최소 횟수를 리턴하라.
"""

def solution(N, K):
    """
    가능한 K를 나누는 과정을 많이 해야한다. -> 그리디 알고리즘
    왜냐하면, 가장 작은 수인 K에 대해서도 1을 빼는 것보다 훨씬 빠르게 1로 수렴시킬수 있기 때문이다.
    """
    ans = 0
    while (N!=1):
        if N % K == 0: # K로 나누어 떨어지는 경우,
            N = N / K
        else:
            N = N - 1
        #print(N)
        ans += 1
    return ans

if __name__ == "__main__":
    N = 25
    K = 5
    print(solution(N, K))