def solution(N):
    """
    245 (생성자) -> 245 + 2+4+5 = 256 (분해합)
    :return: 가장 작은 생성자 구하기

    """
    # 적당한 범위를 지정하고 해당 범위 내의 생성자를 모두 구한다.
    ## 입력값이 10^3 자리인 경우, 10^2 ~ 10^3 안으로 하면 될듯?
    num_of_10 = len(str(N)) # 216 이면 3 이 나옴.
    ans = 0

    # 한자리 숫자면?
    if num_of_10 == 1:
        for n in range(1, N):
            generator_num = n + sum([int(i) for i in str(n)])
            if generator_num == N:
                ans = n
                break

    # 3자리수이면, 2자리부터 3자리 (해당 숫자 전까지) 의 모든 경우의 수를 구함.
    else:
        for n in range(10**(num_of_10 - 2), N):
            generator_num = n + sum([int(i) for i in str(n)])

            # 분해합이 N이면, 해당 숫자는 생성자이다.
            ## 차례대로 생성하기 때문에, 처음 생성되는 경우가 제일 작은 생성자이다.
            if generator_num == N:
                ans = n
                break

    #print(ans)
    return ans

if __name__ == "__main__":
    N = int(input())
    print(solution(N))

