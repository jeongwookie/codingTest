def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        total_cutted_height = sum([tree - mid for tree in trees if tree >= mid])
        if total_cutted_height >= target: # 최소 target 이상 확보하기 성공 -> 더 올렸을 때도 가능할까 확인
            answer = mid # height 저장
            start = mid + 1
        else: # 최소 target 이상 확보 실패 -> height를 더 아래로 조절해서 확인
            end = mid - 1
    return answer

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    num_of_tree, target = map(int, readline().split()) # target의 볌위가 20억까지
    trees = list(map(int, readline().split()))
    trees.sort()

    # 최소 target만큼의 타겟을 확보하기 위햔 height 계산하기
    ## 절단기의 height 자체를 이분 탐색으로 찾아보자
    start, end = 0, trees[-1]
    print(binary_search(start, end))

