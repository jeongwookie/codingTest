if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, target = map(int, readline().split()) # array 크기가 100만까지, 탐색하고싶은 x는 1억단위
    array = list(map(int, readline().split())) # sorted 되어 있는 상태

    from bisect import bisect_left, bisect_right
    count = bisect_right(array, target) - bisect_left(array, target) # 특정 수의 개수 구하기

    # 결과 프린트
    if count == 0:
        print(-1)
    else:
        print(count)


