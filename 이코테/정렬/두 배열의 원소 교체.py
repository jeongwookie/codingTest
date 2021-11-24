if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, K = map(int, readline().split())
    array_a = [int(i) for i in readline().split()]
    array_b = [int(i) for i in readline().split()]

    # array_a를 작은 값으로 나열
    # array_b를 큰값으로 나열
    array_a.sort()
    array_b.sort(reverse=True)

    # 앞에서부터 바꾸는데 총 K번 수행하기
    count = 0
    idx = 0
    while count < K:
        if array_a[idx] < array_b[idx]:
            array_a[idx], array_b[idx] = array_b[idx], array_a[idx]
            count += 1
            idx += 1

    # print sum
    print(sum(array_a))
