"""
8 x 8 로 주어진 판을 잘랐을 때,
체스판을 만들 수 있도록 칠하는 정사각형의 최소값 리턴
N,M은 8이상이고 50이하임
slicing 을 50*50 수행할 수 있네. 큰 범위는 아닌 것 같음.

1. 8 by 8 짜리 체스판을 만들수 있는 모든 경우를 idx로 리턴
2. 해당 idx를 받아서 그 안에 값을 읽고 W로 시작하는 경우와 B로 시작하는 경우를 나누어 min값을 리턴

"""
def solution(N, M, boards): # N은 행의 갯수, M은 열의 갯수
    _list = []
    # 체스판의 시작점이 될 수 있는 경우의 수
    for a in range(N - 7):
        for b in range(M - 7):
            start_with_white, start_with_black = 0,0

            # 시작점 (a,b) 에 맞추어서 8*8로 자름
            for i in range(a, a+8):
                for j in range(b, b+8):

                    # 번갈아가면서 검사하는 방법 : (행+열) % 2 로 case를 나누면 됨.
                    if ((i + j) % 2 == 0): # 인덱스 짝수합
                        if boards[i][j] != "W": # W가 아닌 경우, W로 시작하는 경우에는 전부 W로 칠해줘야함.
                            start_with_white += 1
                        if boards[i][j] != "B": # B가 아닌 경우, B로 시작하는 경우에는 전부 B로 칠해줘야함.
                            start_with_black += 1

                    else: # 인덱스 홀수합. 짝수합의 경우와 반대로 칠해야함.
                        if boards[i][j] != "B": # B가 아닌 경우, W로 시작하는 경우에는 전부 B로 칠해줘야함.
                            start_with_white += 1
                        if boards[i][j] != "W": # W가 아닌 경우, B로 시작하는 경우에는 전부 W로 칠해줘야함.
                            start_with_black += 1


            _list.append(min(start_with_white, start_with_black))

    #print(_list)
    return min(_list)

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N, M = map(int, readline().split())
    boards = []
    for _ in range(N):
        boards.append(readline().strip())
    print(boards)
    print(solution(N, M, boards))