def solution(N):
    if N == 0:
        return 1
    else:
        return N * solution(N-1)

if __name__ == "__main__":
    N = int(input())
    print(solution(N))