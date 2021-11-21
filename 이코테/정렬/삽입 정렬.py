"""
삽입 정렬 : 가장 왼쪽의 원소를 기준으로, 해당 부분이 이미 정렬되어 있다고 가정하고 차례대로 다음 원소들을 뽑아 삽입하는 정렬
예시) 아래 array에서 7은 이미 정렬되어 있다 가정. 5부터 뽑아서 7의 왼쪽일지 오른쪽일지 판단 후 삽입
선택 정렬과 마찬가지로 O(N*2) 인데, 최선의 경우 O(N)임. 거의 정렬된 상태의 데이터라면 아주 빠르게 동작 가능.
"""

array = [7,5,9,0,3,1,6,2,4,8]

def insertion_sort(array):
    for i in range(1, len(array)): # 두번째 원소부터
        for j in range(i,0,-1):
            if array[j] < array[j-1]: # 현재 원소의 위치 : j -> 앞에 녀석과 비교 후 앞이 더 크면 자리 바꿈
                array[j], array[j-1] = array[j-1], array[j] # 한칸씩 왼쪽으로 이동
            else:
                break # 더이상 앞이 크지 않을 경우까지 반복함
    return array

print(insertion_sort(array))