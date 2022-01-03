# for문을 여러개 계속 해서 사용해야 한다.
## 언제 백트래킹 기법을 사용하는건지 자세히 볼 필요가 있다. (아직 뭐가 다른지 이해 못함)
def backtracking():
    if len(stack) == M:
        for i in stack:
            print(i, end=' ')
        print()
        return

    for n in range(1, N+1):
        stack.append(n) # 해당 자식 노드를 stack에 저장 후
        backtracking() # 백트래킹
        stack.pop() # 다시 revert

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split())

    # 중복 가능한 순열 백트래킹으로 출력하기
    stack = []
    backtracking()
