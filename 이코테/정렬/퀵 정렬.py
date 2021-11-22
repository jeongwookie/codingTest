"""
퀵 정렬 : 전체적으로 분할 정렬. 평균적으로 O(NlogN)이며 최악의 상황에서는 O(N**2)의 시간복잡도를 가짐
    1. 어떤 특정한 기준으로 기준값 (pivot)을 정함. 별다른 기준이 없다면 가장 왼쪽 원소를 기준값으로 설정
    2. 포인터를 두개 설정하는데 기준값을 제외한 가장 왼쪽을 left, 가장 오른쪽을 right 로 지정
    3-1. 왼쪽부터 오른쪽으로 left 포인터를 이동시키면서 기준값보다 큰 값을 선택함 (ex. 7)
    3-2. 오른쪽부터 왼쪽으로 right 포인터를 이동시키면서 기준값보다 작은 값을 선택함 (ex. 4)
    4. 3번 과정에서 선택된 두 데이터의 위치를 변경함.
    5. 2~5 과정을 반복한다.
    6-1. 5번 과정을 수행하던 도중, left 포인터가 right 포인터 보다 오른쪽에 있는 (엇갈리는) 경우가 발생하게 된다.
    6-2. 해당 경우가 발생하면, 작은 데이터 (right)와 pivot 데이터의 위치를 바꾼다.
    => 여기까지 하면, 데이터가 두 부분으로 분할된다! (pivot을 기준으로 데이터 묶음이 divide됨)
    => 이후, 각 부분에 대해서 위의 과정을 재귀적으로 수행한다.
    => 각 부분의 원소의 갯수가 1이 되면, 과정을 종료시키면 끝.
"""

def quick_sort(array, start, end):
    # 종료 조건 : 왼쪽에서 시작하는 start 포인터의 위치와 오른쪽에서 시작하는 end 포인터의 위치가 같거나 엇갈리면
    if start >= end:
        return

    # 초기값 지정
    pivot = start # 기준 값을 가장 왼쪽 원소로 지정
    left = start + 1
    right = end

    while (left <= right):
        # left 포인터가 끝을 넘어가지 않고, left가 가리키는 값이 pivot값보다 큰 지점 찾기
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # right 포인터가 끝을 넘어가지 않고 (start+1), right가 가리키는 값이 pivot값보다 작은 지점 찾기
        while (right > start and array[right] >= array[pivot]):
            right -= 1

        if (left > right): # 서로 엇갈린 경우, 작은 데이터와 pivot 값을 교체함
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우, 작은 데이터와 큰 데이터를 교체함
            array[left], array[right] = array[right], array[left]

    # 분할 이후, 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    ## right에 이전 pivot값의 위치가 기록되어 있으므로, right-1 과 right+1 로 나누면 됨.
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

if __name__ == "__main__":
    array = [5,7,9,0,3,1,6,2,4,8]
    quick_sort(array, 0, len(array) - 1)
    print(array)
