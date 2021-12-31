def combination():
    # 종료조건
    if len(stack) == M:
        [print(i, end=' ') for i in stack]
        print()
        return

    # 인접 노드 탐색
    for i in range(1, N+1):
        if i in stack: # stack에 이미 있는 원소의 경우 제외함
            continue
        else:
            if len(stack) == 0 or stack[-1] < i: # 아예 비었으면 그냥 넣고, 안비었을 경우 대소비교
                stack.append(i)
                combination()
                stack.pop() # revert


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split())

    stack = []
    combination()