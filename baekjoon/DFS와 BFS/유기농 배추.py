def dfs(x, y):
    # 범위 밖으로 나가면 False
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return False

    # 해당 좌표에 배추가 없으면 False
    if graph[x][y] == 0:
        return False
    # 해당 좌표에 배추가 없으면 True
    else:
        # 방문처리
        graph[x][y] = 0

        # 상하좌우로 탐색
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

        return True


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(10000) # recursion error 때문에 기입
    T = int(readline().strip()) # num of test case, 여러개의 for문으로 인풋을 받아야함.

    for _ in range(T): # 테스트 케이스에 대해서 아래 모든 프로세스를 돌림
        M, N, K = map(int, readline().split())  # 가로, 세로, 배추 위치 갯수 , 10 8 17
        graph = [[0 for col in range(M)] for row in range(N)] # 초기화

        # 배추 위치 입력 받기
        for _ in range(K):
            x, y = map(int, readline().split())
            graph[y][x] = 1 # 배추가 있는 곳은 1
        #print(graph)

        # dfs 진행
        count = 0
        for i in range(N): # 8
            for j in range(M): # 10
                """
                궁금한점. graph를 나는 밖에서 정의하였고, dfs 함수 내부에서는 정의하지 않았다.
                그러면 dfs 함수 내부에서 graph가 없으니까 밖에서 graph가 있는지 보고 있으면 그걸 가져와서 연산에 사용할 것인데,
                dfs가 돌아가면서 graph값 또한 업데이트가 계속 이루어져야 한다 (내가 의도한대로 할려면)
                이게 지금 되고 있는 것 같은데, 왜 되는가?
                """
                if dfs(i,j): # True이면 -> 배추를 찾았고, 인근에 없을때까지 dfs 진행한 것
                    count += 1
        # 결과 출력
        print(count)
