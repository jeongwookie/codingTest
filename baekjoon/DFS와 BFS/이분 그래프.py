def dfs(start_v, before_color):
    if colored[start_v] == 0:
        colored[start_v] = before_color * (-1) # -1, 1 번갈아가며 칠하기

    # 인접 확인 -> 인접한 애들은 반드시 다른 색으로 칠해야함.
    for i in graph[start_v]:
        if colored[i] == 0:  # 첫 방문 일 경우,
            dfs(i, colored[start_v])
        else: # 첫 방문이 아닌 경우, 컬러를 확인함.
            if colored[i] == colored[start_v]: # 인접한 두 정점의 컬러가 동일하면,
                return False

    return True


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    sys.setrecursionlimit(100000)
    num_of_test_case = int(readline().strip())
    for _ in range(num_of_test_case):
        # 각 케이스에 대해서 인풋 입력
        V, E = map(int, readline().split()) # 정점의 개수, 간선의 개수
        graph = [[] for _ in range(V+1)] # 0번째 인덱스를 사용하지 않기 위해서 한칸 추가 입력
        for _ in range(E):
            v1, v2 = map(int, readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
        graph = [sorted(i) for i in graph]

        # 이분 그래프임을 판별해야함.
        ## 이분 그래프에 대해서 찾아보니, 모든 꼭지점을 빨간색, 파란색으로 칠하되 인접한 꼭지점은 항상 반대로 칠해야 한다는 조건.
        colored = [0 for _ in range(V+1)] # 초기화
        boolean_result = True
        for i in range(1, V+1):
            if not dfs(i, -1): # -1 (파란색) 을 초기값으로 지정 -> start_v에는 빨간색 (1)부터 칠하게 됨.
                boolean_result = False
                break

        # 결과 출력
        if boolean_result:
            print("YES")
        else:
            print("NO")

