if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque
    N, K = map(int, readline().split())
    queue = deque([i for i in range(1, N+1)])

    # K번째를 계속 뽑아낸다.
    answer = []
    while queue:
        queue.rotate(-(K-1)) # K-1 칸씩 왼쪽으로 이동
        answer.append(queue.popleft())

    # 결과 출력
    print("<", end='')
    for idx, n in enumerate(answer):
        if idx == len(answer)-1:
            print(n, end='')
        else:
            print(n, end=', ')
    print(">", end='')