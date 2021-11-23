def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    # pivot 지정
    pivot = array[0] # 가장 왼쪽 원소
    tail = array[1:] # 가장 왼쪽 원소를 제외한 나머지

    # pivot 기준으로 left, right 분할하기
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할 이후, 각 side에서 각각 정렬 수행 후 합치기
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [5,7,9,0,3,1,6,2,4,8]
print(quick_sort(array))