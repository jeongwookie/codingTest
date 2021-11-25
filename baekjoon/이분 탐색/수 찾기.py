def find_num(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target: # 좌측 탐색
            end = mid - 1
        else: # 우측 탐색
            start = mid + 1
    return 0


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    N_list = [int(i) for i in readline().split()]
    M = int(readline().strip())
    M_list = [int(i) for i in readline().split()]

    # 이분 탐색 활용하기
    ## sort부터
    N_list.sort()
    for num in M_list:
        print(find_num(N_list, num, start=0, end=N-1)) # print out 1 or 0

