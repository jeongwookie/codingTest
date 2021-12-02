if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque
    K = int(readline().strip())
    stack = deque([])
    for _ in range(K):
        input = int(readline().strip())
        if input == 0:
            stack.pop()
        else:
            stack.append(input)

    # print out
    print(sum(stack))
