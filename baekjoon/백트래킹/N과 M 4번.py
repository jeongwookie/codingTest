# 조건이 달린 브루트포스 알고리즘
## 그림으로 그렸을 때 가지처럼 뻗어나가되, 특정 조건을 만족하면 돌아와야 하는 경우 사용함
def backtracking():
    # 종료 조건
    if len(stack) == M:
        for i in stack:
            print(i, end=' ')
        print()
        return

    # 노드 방문
    for n in range(1, N+1):
        if len(stack) == 0: # 비어있다면,
            stack.append(n)
            backtracking()
            stack.pop()
        else: # 비어있지 않다면, 비내림차순임을 확인해야함
            if stack[-1] <= n: # 조건을 만족하는 경우만 방문함
                stack.append(n)
                backtracking()
                stack.pop()


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split())

    stack = []
    backtracking()