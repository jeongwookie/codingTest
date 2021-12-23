if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    mapping_array = []
    for _ in range(N):
        mapping_array.append(list(map(int, readline().split())))
    mapping_array.sort()

    # 어떻게 교차한 상황을 인지할 수 있을까?
    # 시작점 A는 어떻게 보면 항상 증가하는 부분 수열의 특성을 가지고 있음 (sort 시)
    # 마찬가지로 매칭되는 끝점 B가 증가하는 부분 수열이면 겹칠 일이 없음
    LIS = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if mapping_array[i][1] > mapping_array[j][1]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    # A는 무조건 전체가 LIS이고, B는 부분이 LIS임.
    ## 이미 LIS를 이루고 있는 곳 빼고 나머지를 끊어주면 해결.
    print(N - max(LIS))