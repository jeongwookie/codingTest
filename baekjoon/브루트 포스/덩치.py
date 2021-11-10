def solution(N, infos):
    """
    :param N: 5
    :param infos: [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
    N이 최소 2이상.
    2개 들어왔는데 둘다 비교가 안될수도 있음. 그러면 둘다 1인거임
    문제의 제한 사항을 보면 N이 50밖에 안됨. 전부다 Brute Force식으로 비교 가능
    for문 두개 돌려버렷
    """
    ans = []
    for i in range(N):
        count = 0
        for j in range(N):
            if i != j: # 자기자신과의 비교는 하지 않음
                if infos[i][0] < infos[j][0] and infos[i][1] < infos[j][1]:
                    count += 1
        #print(f"{i}보다 큰놈 숫자 : {count}")
        ans.append(count+1)

    return ans

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline())
    infos = []
    for _ in range(N):
        cm, kg = map(int, readline().split())
        infos.append([cm, kg])
    print(' '.join(map(str,solution(N, infos)))) # 공백으로 띄워서 프린트
    # for i in solution(N, infos):
    #     print(i, end=' ') # 이런식으로도 프린트 가능.