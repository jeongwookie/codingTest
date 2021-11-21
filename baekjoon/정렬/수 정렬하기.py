if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    import heapq

    N = int(readline().strip())
    heap = []
    for _ in range(N):
        heapq.heappush(heap, int(readline().strip()))

    # return
    while heap:
        print(heapq.heappop(heap))