if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque

    N = int(readline().strip())
    queue = deque([i for i in range(1, N + 1)])

    while (len(queue) > 1):
        queue.popleft()
        move_num = queue.popleft()
        queue.append(move_num)

    print(queue[0])



