"""
"55-50+40"
괄호를 쳐서 최소를 만드는 법. -를 적절히 사용해서 묶어줘야함.
"55-50-25+45+25-45"
- 뒤에 다음 - 가 나올때까지 묶어주면 됨.
문제가 이상하다. 분명히 인풋에 마지막은 숫자라고 되어있는데 공백이 들어가는 경우도 포함되어있는듯;;;
input().strip() 하니까 런타임 에러가 해결되었다.
"""
def convert(string):
    num = ""
    _list = []
    for c in string:
        if c.isdigit():
            num += c  # num에 붙여주기
        else:
            _list.append(num)  # 완성된 숫자 string으로 저장
            num = ""  # 초기화
            _list.append(c)  # 부호 저장

    if num != "":  # 제일 뒤 숫자를 마지막으로 저장함
        _list.append(num)

    return _list

def solution(string):
    #1. string을 숫자와 문자로 구별해서 list화
    function_list = convert(string)
    print(function_list)

    #2. 연산 수행 "55-50+40" "- 50 - 25 + 45 + 25 - 45"
    ## -가 등장하는 순간, 그 뒤의 +를 전부 -로 바꿔줌 (괄호묶기)
    ans = int(function_list[0]) # 초기값
    minus_adding = False
    for i in function_list[1:]:
        if i == "-":
            minus_adding = True
        elif i == "+":
            pass
        else: # 숫자인 경우
            if minus_adding:
                ans -= int(i)
            else:
                ans += int(i)

    return ans

if __name__ == "__main__":
    import sys; input = sys.stdin.readline
    string = input().strip()
    print(solution(string))
