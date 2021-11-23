def solution(input_list):
    # 산술 평균 구하기
    avg = sum(input_list) / N
    print(round(avg))

    # 중앙값 구하기
    sorted_list = sorted(input_list)
    print(sorted_list[N//2])

    # 최빈값 구하기
    count = Counter(sorted_list).most_common()
    max_count = count[0][1]
    max_count_list = [(value, count) for value, count in Counter(sorted_list).most_common() if count == max_count]

    if len(max_count_list) == 1:
        print(max_count_list[0][0])
    else:
        print(max_count_list[1][0])

    # 범위 출력하기
    range = sorted_list[-1] - sorted_list[0]
    print(range)

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import Counter
    N = int(readline().strip())
    input_list = []
    for _ in range(N):
        input_list.append(int(readline().strip()))

    # 리턴
    solution(input_list)

