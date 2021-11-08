def solution(string):
    upper_case_string = string.upper()
    _dict = {}

    # 1 string
    if len(upper_case_string) == 1:
        return upper_case_string

    for s in upper_case_string:
        if _dict.get(s):
            _dict[s] += 1
        else:
            _dict[s] = 1

    _list = sorted([(k,v) for k,v in _dict.items()], key=lambda x: x[1], reverse=True)

    # 최대값 판별
    first = _list[0]
    second = _list[1]
    if first[1] == second[1]:
        return "?"
    else:
        return first[0]

if __name__ == "__main__":
    string = input()
    print(solution(string))
