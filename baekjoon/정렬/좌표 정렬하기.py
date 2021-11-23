if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    points = []
    for _ in range(N):
        points.append(list(map(int, readline().split())))

    for x,y in sorted(points):
        print(x, end=" ")
        print(y)
