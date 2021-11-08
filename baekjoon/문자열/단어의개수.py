def solution(string):
    """
    단어 갯수 세기
    :param string:
    :return: int:
    """
    # 일단 입력된 스트링 좌우 공백을 제거
    string = string.strip()

    # 아예 공백만 입력된 경우,
    if len(string) == 0:
        return 0

    _list = string.split(" ") # 공백으로 단어 체크
    return len(_list)

if __name__ == "__main__":
    string = input()
    print(solution(string))