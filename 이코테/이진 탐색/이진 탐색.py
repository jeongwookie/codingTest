def binary_search(array, target, start, end):
    # 더이상 나눌 수 없는 작은 단위 정의
    ## 여기까지 왔는데 target을 못찾은 경우 : None 반환
    if start > end:
        return None

    mid = (start + end) // 2 # 이걸 왜 -로 착각했지;;;

    if array[mid] == target:
        return mid + 1 # 1번째부터 시작하므로 마지막에 + 1
    elif array[mid] > target: # 좌측 탐색 필요
        return binary_search(array, target, start, mid-1)
    else: # 우측 탐색 필요
        return binary_search(array, target, mid+1, end)

def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] > target: # 좌측 탐색 필요
            end = mid - 1
        else: # 우측 탐색 필요
            start = mid + 1

    return None # loop에서 리턴이 이루어지지 않으면, 해당 원소를 발견 못한 것


if __name__ == "__main__":
    N, target = 10, 7
    array = [1,3,5,7,9,11,13,15,17,19] # sorted 되어있는 상태여야 함

    start = 0
    end = N-1
    print(binary_search_loop(array, target, start, end))