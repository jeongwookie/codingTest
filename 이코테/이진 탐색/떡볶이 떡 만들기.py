"""
현재 이 높이로 지르면 조건을 만족할 수 있는가? -> 예/아니오 에 따라서 탐색 범위를 좁혀서 해결할 수 있다.
=> 문제를 읽어보면, H의 범위가 0부터 10억까지의 정수 중 하나임 (너무 넒다..!) => 큰 탐색범위이면 가장 먼저 이진탐색을 떠올려야 한다!
=> 이진 탐색으로 탐색 범위를 줄여가면서 mid값이 조건을 만족하는가? 에 따라서 과정을 반복하면 된다.
=> 중간점의 값은 시간이 지날수록 '최적화된 값' 이 되기 때문에 과정을 반복하면서 조건을 만족할때마다 해당 값을 기록하면 됨.
"""

def find_max_height(array, target, start, end): # 이진탐색
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum_of_ttuck = sum([i-mid for i in array if i >= mid])
        if sum_of_ttuck >= target: # 조건을 만족하는 경우, 결과를 저장하고, 배열의 오른쪽으로 더 옮겨본다.
            result = mid # 배열에 저장하지 않고 그냥 값을 저장하는 이유는, 오른쪽으로 더 이동했는데 조건을 만족하면 그게 곧 max값이기 때문이다.
            start = mid + 1
        else: # 작은 경우, 결과를 저장하지 않고, 배열의 왼쪽으로 옮겨본다.
            end = mid - 1

    # 결과값 중에서 가장 max 값이 이미 저장되어 있다.
    return result

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split())
    array = [int(i) for i in readline().split()]

    array.sort()
    start = 0
    end = array[-1] # max 값
    print(find_max_height(array, M, start, end))





