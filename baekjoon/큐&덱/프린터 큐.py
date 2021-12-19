if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque
    test_cases = int(readline().strip())
    for _ in range(test_cases):
        num_of_docs, target = map(int, readline().split())
        priority = list(map(int, readline().split()))

        # target 표시해서 queue 구성
        queue = deque()
        for idx, val in enumerate(priority):
            if idx == target:
                queue.append([True, val])
            else:
                queue.append([False, val])

        count = 0
        while queue:
            target_boolean, curr_val = queue.popleft()
            if queue:
                remain_max_val = max([val for boolean, val in queue])
            else:
                remain_max_val = 0 # queue가 비었을때는 0으로 만들어버림
            if curr_val >= remain_max_val: # 인쇄하는 경우
                count += 1
                # 인쇄하는 문서가 target일때,
                if target_boolean:
                    break
            else:
                # 다시 큐에 넣기
                queue.append([target_boolean, curr_val])

        # 결과 출력
        print(count)
