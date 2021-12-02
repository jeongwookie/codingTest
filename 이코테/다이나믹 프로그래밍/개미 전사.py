if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_warehouse = int(readline().strip())
    foods = list(map(int, readline().split()))

    # 얻을 수 있는 식량의 최댓값 출력하기
    """
    1. 작은 문제들을 해결해서 큰 문제를 자동으로 해결할 수 있는가?
    2. 반복적으로 풀어야 하는 문제들인가?
    => dp 테이블에 저장할 i번째 : i번째 식량 창고까지의 최적의 해라고 정의하자!
    => i번째 식량 창고를 터는 경우 or 안터는 경우 단 두가지만 정의할 수 있음. 이걸로 점화식 만들면 끝
    """
    dp = [0 for _ in range(len(foods))] # dp 테이블 만들기

    # 최소 N은 3부터 시작. 바텀업 방식으로 dp 구성해보기
    dp[0], dp[1] = foods[0], max(foods[0], foods[1])
    for i in range(2, len(foods)):
        dp[i] = max(dp[i-1], dp[i-2] + foods[i])

    print(dp[num_of_warehouse-1])

