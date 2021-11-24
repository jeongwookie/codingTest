if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    info = []
    for idx in range(N):
        age, name = readline().split()
        info.append([int(age), name, idx])

    # sort
    info.sort(key=lambda x: (x[0], idx))

    # print
    for age, name, _ in info:
        print(age, end=' ')
        print(name)