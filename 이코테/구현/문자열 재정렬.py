"""
숫자와 알파벳이 섞인 문자열이 인풋으로 들어왔을때,
알파벳을 오름차순으로 정렬해서 출력하고 이어서 숫자를 모두 더해서 붙여준 스트링을 출력하라.
"""

"""
주어진 char이 알파벳인지 확인하는 함수가 있다?!
c.isalpha() -> True이면 알파벳임..
''.join(list) 하면 리스트 내의 원소들을 스트링으로 하나씩 다 붙여버린다.
"""
def solution(string):
    string = sorted(string) # 오름차순으로 정렬
    ans = ""
    _sum = 0
    _str = ""
    for c in string:
        if ord(c) <= ord("9"): # 숫자인 경우
            _sum += int(c)
        else: # 문자인 경우
            _str += c
    ans += _str + str(_sum)
    return ans

if __name__ == "__main__":
    print(solution(string="AJKDLSI412K4JSJ9D"))
