if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    array_size = int(readline().strip()) # 10만까지
    target = int(readline().strip()) # 10억
    """
    A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.
    (1,1) (1,2) ... (3,2) (3,3)
    최소가 1이고 최대가 9임 -> 이런 일차원 array를 만들고 카운트 해야할듯?
    근데 그냥 만들면, 5같은 애들은 원래 만들수 없는건데.. 어케 거름?
    """
    start = 1
    end = target # 7
    answer = 0
    while start <= end:
        mid = (start + end) // 2 # 4보다 작거나 같은 숫자는 어레이에서 몇개일까?

        count = 0 # 전체 array에서 mid보다 작거나 같은 숫자가 몇개인지 다 세줌
        for i in range(1, array_size+1): # 1부터 3까지 루프. 각 행은 배수로 이루어져 있음.
            count += min(mid // i, array_size) # 최대 array_size만큼 선택됨. 그 이상은 범위를 벗어남.

        if count >= target: # 만약 count가 target보다 크거나 같으면, 왼쪽으로 이동
            answer = mid # 저장
            end = mid - 1
        else: # 오른쪽으로 탐색
            start = mid + 1

    print(answer)





