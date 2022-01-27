import heapq

def heapsort(iterable): # O(NlogN)
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 : O(logN)
    for val in iterable:
        heapq.heappush(h, val) # 기본적으로 min heap
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)