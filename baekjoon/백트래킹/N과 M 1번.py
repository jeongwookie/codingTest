"""
backtracking: DFS 기반. stack 및 재귀를 활용함
1. 종료조건
2. for loop
3. loop 내 재귀함수 호출 시 가지치기 (불필요한 반복을 제거)
"""


# 반복적으로 숫자를 선택해서 M개까지 골라, 수열을 완성한다.
def combination():
    # 정답이라면?
    if len(stack) == M:
        [print(str(c), end=' ') for c in stack] # 출력
        print('')
        return

    # 정답이 아니라면?
    for i in range(1, N + 1): # 뻗을 수 있는 모든 자식 노드에 대해서
        if i not in stack: # 정답이 될 수 있는 노드라면,
            stack.append(i) # stack에 해당 자식노드를 저장
            combination() # 재귀 함수 수행
            stack.pop() # 다시 부모 노드로 리턴 (원래의 값으로 복구)


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split())

    # 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
    ## 백트래킹으로 구현
    ## 백트래킹은 DFS의 방식을 기반으로, 불필요한 경우를 배제하며 원하는 해답에 도달할 때까지 탐색하는 방법
    stack = []
    combination()

