if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    array = list(map(int, readline().split()))

    ## 바이토닉 수열 구하기
    ## 증가만 하거나, 감소만 하거나, 증가 감소가 한번만 이루어지는 수열
    ## LIS를 왼쪽으로 한번, 오른쪽으로 한번 구해서 두개를 더한 것이 가장 큰 수가 나오면?

    left_lis = [1 for _ in range(N)] # 해당 인덱스에서 끝나는 가장 긴 부분 수열의 길이
    right_lis = [1 for _ in range(N)]

    # left LIS 구하기
    for i in range(1, N):
        for j in range(i):
            if array[i] > array[j]: # 증가하는 수열이면,
                left_lis[i] = max(left_lis[i], left_lis[j] + 1) # left_lis[i] 값 누적시키기

    # right LIS 구하기
    reverse_array = array[::-1]
    for i in range(1, N):
        for j in range(i):
            if reverse_array[i] > reverse_array[j]: # 증가하는 수열이면,
                right_lis[i] = max(right_lis[i], right_lis[j] + 1) # right_lis[i] 값 누적시키기
    right_lis.reverse() # 반대로

    # 가장 긴 바이토닉 수열 구하기
    ## 두 리스트를 더해서 최대가 나오는 지점이 S(k)이므로, 더한 값의 -1을 해주면 결과를 얻을 수 있음
    bitonic_lis = [i+j for i,j in zip(left_lis, right_lis)]
    print(max(bitonic_lis) - 1)
