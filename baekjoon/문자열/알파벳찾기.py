def solution(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    _dict = {}
    # 초기화
    for c in alphabet:
        _dict[c] = -1

    # 입력
    # 처음 등장할때만 기록
    for idx, s in enumerate(string):
        if _dict[s] == -1:
            _dict[s] = idx

    # 리턴
    return [i for i in _dict.values()]


if __name__ == "__main__":
    string = input()
    print(*solution(string))

