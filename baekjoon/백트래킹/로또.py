def lottery(idx, x):
    if x == 6:
        # 방문한 노드만 출력함
        for j in range(len(S)):
            if visited[j]:
                print(S[j], end=' ')
        print()
        return

    else:
        for i in range(idx, k): # S의 인덱스, 0~5
            if not visited[i]: # 방문한 적이 없는 노드라면,
                visited[i] = 1 # 방문 처리
                lottery(i + 1, x + 1) # 다음 idx부터
                visited[i] = 0 # revert


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    while True:
        _list = list(map(int, readline().split()))
        if _list[0] == 0: # 종료
            break

        k, S = _list[0], _list[1:]
        visited = [0 for _ in range(k)]
        lottery(0, 0)
        print()
