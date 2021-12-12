if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    size = int(readline().strip()) # 5

    triangle = []
    for _ in range(size):
        triangle.append(list(map(int, readline().split())))

    # 인덱스가 변할때 dp에 저장할 값의 크기도 이에 맞게 변경하는 방식의 다이나믹 프로그래밍
    dp = [[0] * (idx+1) for idx in range(size)]

    # level 0 : 초기값
    dp[0][0] = triangle[0][0]

    # 이중 for문 돌면서 전범위 탐색
    for level in range(1, size): # level 에 대한 loop
        for i in range(level+1): # level 내의 인덱스 루프
            if i == 0: # 왼쪽 끝은 max값을 계산할 필요가 없음
                dp[level][i] = dp[level-1][i] + triangle[level][i]

            elif i == level: # 오른쪽 끝은 max값을 계산할 필요가 없음
                dp[level][i] = dp[level-1][i-1] + triangle[level][i]

            else: # 중간의 경우, 앞 레벨의 좌우를 비교해야함 (max)
                dp[level][i] = max(dp[level-1][i-1], dp[level-1][i]) + triangle[level][i]

    # 답 리턴
    print(max(dp[size-1]))
