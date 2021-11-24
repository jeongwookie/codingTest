if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    input_array = list(map(int, readline().split()))
    sorted_set_array = sorted(list(set(input_array)))

    # dict으로 해당 숫자의 순서를 저장
    _dict = {sorted_set_array[i]:i for i in range(len(sorted_set_array))}

    # print
    for num in input_array:
        print(_dict.get(num), end=' ')


