if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    array = list(map(int, readline().split()))

    # 전에 이진탐색으로 풀었던 문제임
    ## dp에 어떤 정보를 저장해야 할까?
    ## dp[i] : array[i]를 마지막 원소로 가질 때, 증가하는 부분 수열의 최대 길이
    ## dp 테이블을 구성할 때 의미를 잘못 이해해서 풀이가 꼬여버렸다 ㅠㅠ
    dp = [1] * (len(array)) # 최소 길이가 1이므로 1로 초기화 (자기 자신)

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] > array[j]: # array[i]가 i 이전의 값보다 클때
                dp[i] = max(dp[i], dp[j] + 1)

    # 끝까지 탐색 후 마지막 값 출력
    print(max(dp))




