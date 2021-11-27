def install_wifi(distance):
    ## 해당 distance 가 최소가 되는, 집들을 count해야하는데
    ## 첫 집을 무조건 선택하는게 이해가 잘 안됐다. 근데 잘 생각해보면 첫집을 선택하지 않으면 num_of_wifi을 max화 시키지 못한다.
    count = 1
    curr = houses[0]
    for i in range(1, num_of_house):  # 모든 집 돌기
        if curr + distance <= houses[i]:  # 기준점으로 처음 설치한 집에서 distance보다 같거나 더 멀리 떨어진 집 발견하면 거기 설치
            count += 1
            curr = houses[i]  # 갱신
    return count

def binary_search(houses, start, end):
    max_dist = 0
    while start <= end:
        mid = (start + end) // 2  # ex. 4
        # num_of_wifi 개의 공유기를 설치해야함.
        # mid라는 거리를 유지하면서 몇개의 공유기를 설치할 수 있는가?
        ## 같거나 더 많이 설치할 수 있다면, 거리를 좀 더 벌려도 됨 -> 우측으로 탐색
        installed_wifi_num = install_wifi(mid)
        if installed_wifi_num >= num_of_wifi:
            start = mid + 1  # 거리를 더 벌려줌. 우측 탐색
            max_dist = mid  # 현재까지의 max 거리 저장
        ## 더 적게 설치할 수 있다면, 거리를 더 좁혀서 탐색해보자 -> 좌측으로 탐색
        else:
            end = mid - 1  # 거리를 더 좁혀줌. 좌측 탐색

    return max_dist

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_house, num_of_wifi = map(int, readline().split()) # target의 범위가 10억 이하 -> 찾으려면 어떻게든 탐색 범위를 줄여야함.
    houses = []
    for _ in range(num_of_house):
        houses.append(int(readline().strip()))

    # num_of_wifi 만큼 선택해서, 결과를 비교해야함.
    # 항상 좌표를 탐색하는 게 아니라, 구하고자 하는 걸 변수로 두고 해당 변수를 이진 탐색하는 방식으로 문제를 재구성한다
    # parametric search 문제로, 어떻게든 O/X로 재구성 해야한다.
    ## 최대 거리를 구해야 하니까.. 거리 자체를 변수로 두고 탐색하는 방법
    houses.sort()

    start = 1 # 어떻게 주어지던 최소 거리는 1
    end = houses[-1] - houses[0] # 주어진 houses 에서 최대 - 최소가 max 거리, ex.8

    # 결과 프린트
    print(binary_search(houses, start, end))



