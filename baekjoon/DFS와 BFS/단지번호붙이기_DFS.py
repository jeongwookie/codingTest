def dfs(x, y):
    if x<0 or x>len(graph)-1 or y<0 or y>len(graph)-1: # (x,y) 가 주어진 범위를 벗어나면 False
        return 0

    if graph[x][y] == 0: # (x,y) 에 집이 없으면 False
        return 0

    else:
        # (x,y) 에 집이 있으면, 방문 처리함
        graph[x][y] = 0
        # 해당 집 기준으로 집이 사방에 없을때까지 재귀적으로 방문
        return 1 + dfs(x, y+1) + dfs(x-1, y) + dfs(x, y-1) + dfs(x+1, y)

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline())
    graph = []
    for _ in range(N):
        read = list(readline().strip())
        graph.append(list(map(int, read)))

    count = 0
    num_of_house = []
    for i in range(N):
        for j in range(N):
            result = dfs(i, j) # 모든 좌표값에 대해서 dfs 수행 -> 단지 내 집 수를 전부 셈
            if result != 0: # 집을 찾은 경우, 단지를 무조건 생성함
                num_of_house.append(result) # 단지 내 집 수 저장
                count += 1 # 단지 수 카운트

    # 결과 출력
    print(count)
    [print(i) for i in sorted(num_of_house)] # 오름차순 정렬
