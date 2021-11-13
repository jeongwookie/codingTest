def dfs(x, y):
    if x<0 or x>len(graph)-1 or y<0 or y>len(graph)-1: # (x,y) 가 주어진 범위를 벗어나면 False
        return False

    if graph[x][y] == 0: # (x,y) 에 집이 없으면 False
        return False

    else:
        # (x,y) 에 집이 있으면, 방문 처리함
        """
        글로벌 변수 사용. 내가 풀이했을 때는 글로벌 변수를 지양하는 방식으로 생각했음.
        글로벌 변수를 사용하고 싶을때는 아래와 같이 함수 안에서 global을 명시해주면 됨.
        """
        graph[x][y] = 0
        global count
        count += 1

        # 해당 집 기준으로 집이 사방에 없을때까지 재귀적으로 방문
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

        return True

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline())
    graph = []
    for _ in range(N):
        read = list(readline().strip())
        graph.append(list(map(int, read)))

    count = 0
    num_of_house_group = 0
    num_of_house = []
    for i in range(N):
        for j in range(N):
            if dfs(i, j): # True일때 : 처음 방문했을 때 0이 아니고, 해당 포인트를 시작으로 재귀적으로 전부 방문했음.
                num_of_house.append(count) # 해당 단지 내 집 수 저장
                count = 0 # 집 수 초기화
                num_of_house_group += 1 # 단지 수 카운트

    # 결과 출력
    print(num_of_house_group)
    [print(i) for i in sorted(num_of_house)] # 오름차순 정렬
