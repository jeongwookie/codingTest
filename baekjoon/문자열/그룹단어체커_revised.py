def solution(string):
    """
    :param string:
    :return: boolean

    그룹 단어 체커. 순서대로 읽어서 boolean값을 전달해주면 된다.
    해당 값의 연속성을 체크해줘야 하는데 흠.. 어떻게 저장해둘까? -> stack으로!
    False 가 하나라도 발견되면 그냥 전체가 False가 된다.
    """
    _dict = {}
    stack = []
    for s in string: # ssa 이면?
        if not _dict.get(s): # 첫번째 char은 반드시 이쪽으로 가기때문에 stack이 빌수는 없음.
            _dict[s] = "True"
        else:
            prev = stack[-1] # 직전의 값을 뽑아옴
            if prev != s:
                _dict[s] = "False"
                return False

        stack.append(s)
    return True

    #print(_dict)
    ## 결과값 출력 -> False가 하나라도 있으면 False!
    # cheked_list = [i for i in _dict.values()]
    # if "False" in cheked_list:
    #     return False
    # else:
    #     return True

if __name__ == "__main__":
    N = int(input())
    answer = []
    for _ in range(N):
        string = input()
        answer.append(solution(string))
    print(len([i for i in answer if i]))