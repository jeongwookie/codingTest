def bfs(x):
    queue = deque([x])
    while queue:
        curr_x = queue.popleft()

        # 현재 좌표가 K와 같으면 종료
        if curr_x == K:
            print(graph[curr_x])
            break

        # 이동할 수 있는 방법에 대한 정의
        dx = [1, -1, curr_x]
        for idx in range(3):
            next_x = curr_x + dx[idx]
            if 0 <= next_x <= 100000:  # 범위 내 : 이게 가장 첫번째 다뤄야할 조건문임. 순서를 잘못함.
                if graph[next_x] == 0: # 처음 방문
                    queue.append(next_x)
                    graph[next_x] = graph[curr_x] + 1 # count 증가


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000)
    from collections import deque
    N, K = map(int, readline().split())

    # 걷거나 순간이동을 통해 가장 빠른 시간안에 K로 이동하는 경우!!
    graph = [0] * 100001 # max. 으악 최대가 10만이 아니라 원소 갯수는 10만 1개였다..!! 인덱스 에러 계속뜸
    if N == K:
        print(0) # 위치가 동일하면 0초
    else:
        bfs(N)

