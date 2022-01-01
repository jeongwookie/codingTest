if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    array = list(map(int, readline().split()))
    array.sort()
    print(array[0] * array[-1])