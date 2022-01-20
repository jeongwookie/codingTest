if __name__ =="__main__":
    import sys; readline = sys.stdin.readline

    # 병사를 배치할때 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
    # 특정한 위치에 있는 병사를 열외
    # 남아있는 병사의 수가 최대

    ## 문제 읽어보니까 LIS 문제이다.
    N = int(readline().strip())
    array = list(map(int, readline().split()))
    array.reverse()
    print(array)

    LIS = [1] * N # 특정 위치에서 문제의 조건을 만족하는 가장 긴 수열의 길이는 최소가 1이다.

    for i in range(1, N):
        # LIS[i] : i번째 원소를 마지막으로 가지는 수열에서 가장 긴 부분수열의 길이
        for j in range(i): # i가 2이면, i 이전 원소 인덱스인 0과 1을 돌면서 비교함
            if array[j] < array[i]: # 현재 값이랑 비교해서 증가하는 수열이면
                LIS[i] = max(LIS[i], LIS[j] + 1) # 값 누적

    # 가장 긴 증가하는 수열을 LIS 리스트에 저장했음
    # 이를 전체에서 빼주면 답
    print(N - max(LIS))

    """
    가장 긴 증가하는 부분수열
    LIS[i] : array[i]를 마지막 원소로 가지는, 증가하는 부분 수열의 최대 길이
    모든 i에 대하여, LIS[i] = max(LIS[i], LIS[j] + 1) if array[j] < array[i] 가 점화식이다.
    가장 긴 감소하는 부분수열을 구할려면 주어진 array 를 reverse() 시킨 후 똑같이 풀어주면 된다.
    주의할 점은 가장 긴 증가하는 부분수열로 점화식은 구성을 해야한다는거!
    """