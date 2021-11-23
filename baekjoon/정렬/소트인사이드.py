def solution(N):
    _list = sorted([int(i) for i in N], reverse=True)
    for n in _list:
        print(n, end='')


if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = readline().strip()
    solution(N)