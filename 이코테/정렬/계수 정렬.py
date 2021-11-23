"""
계수 정렬 (count sort) : 각 원소의 등장 횟수를 센다음 해당 횟수만큼 인덱스를 출력하면 그것이 정렬의 결과물과 같아짐.
-> 시간 복잡도의 경우 최악의 경우에도 O(N + K)라서, K가 제한되어 있는 경우에 매우 빠른 속도를 보여줌.
-> K는 데이터의 최댓값을 의미함. 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 (0,1,2,3,..) 표현할 수 있을 때 사용가능!
"""

def count_sort(array):
    # 먼저 array의 max값을 파악하여 공간 확보
    count = [0 for _ in range(max(array)+1)]

    # array를 읽으면서 count 진행
    for num in array:
        count[num] += 1 # 해당 인덱스에 1씩 추가하여 숫자 세기

    # 결과 출력하기
    result = []
    for idx in range(len(count)): # count의 크기만큼 인덱스를 확인
        for c in range(count[idx]): # count에 실제로 저장되어있는 count 수만큼 루프
            result.append(idx)

    return result

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
print(count_sort(array))