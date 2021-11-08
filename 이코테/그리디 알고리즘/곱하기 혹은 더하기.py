"""
숫자 사이에 x 혹은 + 연산자를 넣어서 결과적으로 만들어 질 수 있는 가장 큰 수를 구해라.
무조건 왼쪽부터 순서대로 연산이 이루어진다.
그리디 알고리즘 : 단순히 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는가?
"""

def solution(S):
    # len(S) - 1 만큼을 연산할 수 있음
    ## 0이나 1이 아닌 이상 다 x 연산 하면 되지 않나? -> 최대한 x을 많이 하면 될듯?
    stack = []
    S_list = [int(i) for i in S]
    while S_list:
        if len(stack) == 0:
            first = S_list.pop(0)
            second = S_list.pop(0)
        else:
            first = stack.pop()
            second = S_list.pop(0)

        if (first in [0, 1]) or (second in [0, 1]): # 0이나 1이 포함되어 있으면, 무조건 + 연산
            result = first + second
        else:
            result = first * second

        stack.append(result)

    return stack.pop()

def solution_2(S):
    result = int(S[0]) # 첫번째 숫자 대입

    for i in range(1, len(S)): # 두번째 숫자부터 인덱스로 읽음
        num = int(S[i])
        # 만약 두 수 중에서 하나라도 0 또는 1이라면 +을 수행함.
        if (result <= 1) or (num <= 1):
            result += num
        else:
            result *= num

    return result

if __name__ == "__main__":
    S = "02984"
    print(solution(S)) # 576
    print(solution_2(S))