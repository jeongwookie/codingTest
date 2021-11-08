def solution(N):
    # 0번째 피보나치
    if N == 0:
        return 0
    # 1번째 피보나치
    elif N == 1:
        return 1
    else:
        return solution(N-1) + solution(N-2)

if __name__=="__main__":
    N = int(input())
    print(solution(N))