def print_each_cases(N):
    """
    dp를 정의할때,
    dp_zero[N] : fibo(N)을 계신했을 때 0이 출력되는 횟수 저장
    dp_one[N] : fibo(N)을 계신했을 때 1이 출력되는 횟수 저장
    bottom-up을 사용할때는 반복문으로 처리.
    """
    dp_zero = [0 for _ in range(40+1)] # max가 40개
    dp_one = [0 for _ in range(40+1)]
    dp_zero[0], dp_zero[1] = 1, 0
    dp_one[0], dp_one[1] = 0, 1
    if N >= 2:
        for i in range(2, N+1):
            dp_zero[i] = dp_zero[i - 1] + dp_zero[i - 2]
            dp_one[i] = dp_one[i - 1] + dp_one[i - 2]

    # 결과 출력
    print(dp_zero[N], end=' ')
    print(dp_one[N])


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    test_cases = int(readline().strip())
    for _ in range(test_cases):
        print_each_cases(int(readline().strip()))