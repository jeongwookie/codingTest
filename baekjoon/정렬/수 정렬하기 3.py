if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    """
    N이 대단히 큰데, 실제로 N의 범위가 10000보다 작거나 같은 자연수이므로 카운트 정렬을 사용할수 있다. O(N+10000)
    """
    count = [0 for _ in range(10000+1)] # Max : 10000
    for _ in range(N):
        input = int(readline().strip())
        count[input] += 1 # 해당 값을 count

    # 출력
    for i in range(len(count)):
        for j in range(count[i]):
            print(i)