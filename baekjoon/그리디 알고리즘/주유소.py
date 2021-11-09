def solution(num_of_city, roads, gas_stations):
    """
    최소값을 갱신하는 코드를 짜보자.
    다음 최소값을 가지는 gas station이 나올때까지 현재 최소값을 만족하는 곳에서 채워넣는다고 계산.
    # gas stations = [5,2,3,1,4]
    # roads = [2,3,1,2]
    """
    gold = 0 # init

    #1. 첫번째 gas station에서는 반드시 기름을 넣어야함.
    min_cost = gas_stations[0]

    for idx in range(num_of_city - 1):
        road = roads[idx]
        gas_station_cost = gas_stations[idx]

        #2. min값을 가진다고 저장해놓은 값보다 더 작은 gas_station_cost가 나오면 거기서 기름 넣는다.
        ## min값을 갱신하여, 그다음에 더 작은 값이 나오기 전까지 다 여기서 기름 넣는걸로 계산한다.
        if min_cost > gas_station_cost:
            min_cost = gas_station_cost

        print(f"gas_station_cost : {gas_station_cost}")
        print(f"road : {road}")
        print(f"min_cost : {min_cost}")
        gold += (min_cost * road)
        print(f"accum gold : {gold}")
        print("===")

    return gold

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_city = int(readline())
    roads = list(map(int, readline().split()))
    gas_stations = list(map(int, readline().split()))

    print(solution(num_of_city, roads, gas_stations))