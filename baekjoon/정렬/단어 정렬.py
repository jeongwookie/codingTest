if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())

    _dict = {}
    result = []
    for _ in range(N):
        string = readline().strip()
        if not _dict.get(string):
            _dict[string] = 1
        else:
            continue
        result.append(string)

    # sort
    result.sort(key=lambda x: (len(x), x))

    # print
    for word in result:
        print(word)