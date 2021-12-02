"""
순서가 중요한 문제네. (다음에 )가 나와야지..
스택이 빈 상태에서 )가 나오면 무조건 아웃이네
처음에 )가 나오는 것도 비슷한 맥락인듯?
"""
def is_vps(string):
    # ()쌍 만들기
    ## stack에는 (만 넣어주고, )을 만나면 stack에서 하나씩 pop해줌
    ## 만약 VPS라면, stack이 비게 될꺼임
    stack = deque([])
    idx = 0
    while idx < len(string):
        curr = string[idx]
        if curr == "(":
            stack.append(curr)
        else: # curr == ")"
            if len(stack) == 0: # stack이 비어있는 상황이라면, )을 처리할 수가 없다.
                return "NO"
            else: # stack이 비어있지 않다면 () 쌍을 만들어 줄 수 있다.
                stack.pop() # (을 하나 뽑아서 쌍을 만든다.
        idx += 1

    # 결과
    if len(stack) == 0:
        return "YES"
    else: # (가 )보다 많이 있을 때 해당 현상이 발생한다.
        return "NO"

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque
    test_cases = int(readline().strip())

    for _ in range(test_cases):
        print(is_vps(readline().strip()))