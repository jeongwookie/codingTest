def solution(N):
    """
    분해합 풀이를 최적화해보자.
    분해합 = 생성자 + (생성자의 각 자릿수)
    생성자 = 주어진 숫자 N - (미지의 생성자 각 자릿수의 합)
    그러므로, 생성자를 브루트 포스로 구하되, 각 자릿수의 최대값을 넣어서 범위를 최소화시킨다.
    :param N:
    :return:
    """
    ## min_range : N의 자릿수만큼 9를 넣어줌.
    min_range = abs(N - (len(str(N)) * 9))
    ans = 0

    if len(str(N)) == 1:
        for n in range(1, N):
            result = n + sum(map(int, str(n)))  # 분해합 구하는 식.
            if result == N:  # 분해합이 주어진 N과 같으면, 해당 n이 최소 생성자임.
                ans = n
                break

    else:
        for n in range(min_range, N):
            result = n + sum(map(int, str(n))) # 분해합 구하는 식.
            if result == N: # 분해합이 주어진 N과 같으면, 해당 n이 최소 생성자임.
                ans = n
                break

    return ans

if __name__ == "__main__":
    N = int(input())
    print(solution(N))