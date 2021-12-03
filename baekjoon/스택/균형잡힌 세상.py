def is_valid(string):
    idx = 0
    stack = deque([])
    while idx < len(string):
        c = string[idx]
        if c == "(" or c == "[": # 여는 괄호는 전부 스택에 넣음
            stack.append(c)
        elif c == ")":  # 닫는 괄호가 나온 경우 스택의 상태를 확인
            if stack:  # 스택이 비어있지 않은 경우,
                if stack[-1] == "(":  # 현재 괄호와 stack 최상단에 저장된 괄호가 짝을 이루는 경우 pop
                    stack.pop()
                else:  # 이루지 않는 경우, 바로 문제가 생김.
                    return "no"
            else:  # 스택이 비어있는 경우, 바로 우리가 원하는 상태가 아님
                return "no"
        elif c == "]":  # 닫는 괄호가 나온 경우 스택의 상태를 확인
            if stack:  # 스택이 비어있지 않은 경우,
                if stack[-1] == "[":  # 현재 괄호와 stack 최상단에 저장된 괄호가 짝을 이루는 경우 pop
                    stack.pop()
                else:  # 이루지 않는 경우, 바로 문제가 생김.
                    return "no"
            else:  # 스택이 비어있는 경우, 바로 우리가 원하는 상태가 아님
                return "no"

        idx += 1  # 괄호가 아닌 경우 포함하여 업데이트

    if not stack:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque

    while True:
        string = readline().rstrip()
        if string == ".": # 종료 조건
            break

        print(is_valid(string))

