"""
구현 문제: 좌표계
주어지는 좌표는 a1 이런식의 string이다. abc는 열이고 123은 행임.
주어진 좌표에서 시작하는 나이트가 갈수 있는 모든 경우의 수를 출력하라.
1. 수평 2번 수직 1번
2. 수직 2번 수평 1번
이런 형태로만 움직일 수 있음.
"""

def solution(string):
    # 일단 입력받은 열 string을 숫자로 바꿔야함.
    alphabet = "abcdefgh"
    x, y = alphabet.index(string[0]) + 1, int(string[1]) # 시작 좌표
    """
    정답을 보니, 이거를 아스키 코드 읽는 방법으로 해결할 수도 있다.
    a -> 1, b -> 2 이런식으로 맵핑 하고 싶다는 건데,
    int(ord(string[0])) - int(ord('a')) + 1 이런식으로.
    """
    # 움직일 수 있는 경우의 수 셋팅
    case_1 = [[-1,-2], [-1,2], [1,-2], [1,2]]
    case_2 = [[-2,-1], [-2,1], [2,-1], [2,1]]
    concat = case_1 + case_2

    count = 0
    for move in concat:
        moved = [i+j for i,j in zip([x,y], move)]
        #print(moved)
        if (1 <= moved[0] <= 8) and (1 <= moved[1] <= 8):
            count += 1

    return count

if __name__ == "__main__":
    print(solution(string="a1"))
