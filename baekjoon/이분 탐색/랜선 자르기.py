"""
문제의 조건 : need_num_of_line을 만족하는 범위 내에서, 최대 자를 수 있는 길이를 정해야 한다.
"""

def find_max_length(lines, target_num, start, end):
    max_height = 1 # 0이 될수는 없네? 무조건 1 이상임.
    while start <= end:
        mid = (start + end) // 2 # 400쯤
        if mid == 0: # zero division 방지
            break
        count = sum([i // mid for i in lines])
        if count >= target_num: # target 넘버와 일치하거나 그거보다 크면 문제의 조건을 만족함. -> 더 큰 mid를 찾아보자.
            max_height = mid # 저장
            start = mid + 1 # 우측 탐색
        else: # 문제의 조건을 만족하지 못함 -> 더 작은 mid를 찾아봐야함.
            end = mid - 1 # 좌측 탐색
    return max_height


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_line, target_num = map(int, readline().split()) # target의 범위가 1백만 이하
    lines = []
    for _ in range(num_of_line):
        lines.append(int(readline().strip()))

    lines.sort() # [457, 539, 743, 802]
    print(find_max_length(lines, target_num, start=0, end=lines[-1]))

