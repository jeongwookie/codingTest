def dfs(depth, total, plus, minus, multiply, divide):
    global minimum, maximum
    if depth == N: # 주어진 수만큼 깊이가 도달한 경우 (끝 수 까지 연산 완료한 경우)
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 각 연산자가 0이 아닐 경우에, depth가 N이 될때까지 dfs
    if plus:
        dfs(depth + 1, total + array[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - array[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * array[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / array[depth]), plus, minus, multiply, divide - 1)

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline().strip())
    array = list(map(int, readline().split()))
    operator = list(map(int, readline().split())) # +, -, x, //

    minimum, maximum = 1e9, -1e9

    # dfs
    dfs(1, array[0], operator[0], operator[1], operator[2], operator[3])
    print(maximum)
    print(minimum)
