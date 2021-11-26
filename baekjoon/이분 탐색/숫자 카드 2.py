def find_num_of_targets_in_cards(array, target):
    left_index = bisect_left(array, target)
    right_index = bisect_right(array, target)
    return right_index - left_index

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from bisect import bisect_left, bisect_right
    num_of_cards = int(readline().strip()) # 50만까지
    cards = [int(i) for i in readline().split()] # 각 숫자는 -1천만 ~ 1천만

    num_of_tests = int(readline().strip()) # 50만까지
    targets = [int(i) for i in readline().split()] # 각 숫자는 -1천만 ~ 1천만

    # 이분 탐색으로 찾기
    cards.sort()
    for target in targets:
        count = find_num_of_targets_in_cards(cards, target)
        print(count, end=' ')
