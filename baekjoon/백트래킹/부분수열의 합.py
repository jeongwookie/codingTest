def dfs(idx):
    #global count
    global answer
    # 종료 조건에 도달한 경우, 크기가 0인 부분수열은 제외해야함
    # 종료 조건에 도달하더라도, 뒤에 array에 0이 있어서 케이스가 증가하는 경우가 있음.
    if sum(stack) == S and len(stack) != 0:
        #count += 1

        answer.add(str(stack[:]))
        #return

    # 모든 노드에 대해서 방문을 완료한 경우 종료
    if len(stack) == N:
        return

    # 노드 차례대로 방문하기
    for i in range(idx, N):
        curr = array[i]
        if not visited[i]:
            visited[i] = 1
            stack.append(curr)

            dfs(i+1)

            visited[i] = 0
            stack.pop()


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, S = map(int, readline().split())
    array = list(map(int, readline().split()))

    #count = 0
    stack = []
    answer = set()
    visited = [0 for _ in range(N)]

    dfs(0)
    print(len(answer))
    #print(count)
