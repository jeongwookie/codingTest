if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    array = []
    for _ in range(N):
        array.append(list(map(int, readline().split())))

    array.sort(key=lambda x: (x[1], x[0]))

    # print
    for x,y in array:
        print(x, end=' ')
        print(y)