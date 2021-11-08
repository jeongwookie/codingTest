"""
N*N 정사각형 공간. 왼쪽 위 좌표계는 (1,1)이고, 가장 오른쪽 아래 좌표계는 (N,N)임
상하좌우 움직일 수 있고, 공간에서 벗어나는 명령은 무시됨.
스트링으로 LRUD가 주어질때, 도착 지점을 리턴하라.
"""

def solution(N, string):
    # (x,y)를 지칭할때, (세로, 가로) 로 생각하면 편하다.
    # LRUD 순. 업다운도 일반적인 의미와 부호가 반대임.
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    command_type = ["L", "R", "U", "D"]

    # 현재 위치
    x, y = 1, 1

    for command in string:
        # L,R,U,D 중 무엇인지 파악
        for idx, move in enumerate(command_type):
            if command == move:
                nx = x + dx[idx]
                ny = y + dy[idx]
        # update 조건
        ## x가 1보다 작거나 N보다 크면 안됨.
        ## y가 1보다 작거나 N보다 크면 안됨.
        if (1 <= nx <= N) and (1 <= ny <= N):
            x,y = nx, ny
        #print(f"(x,y) : {x,y}")

    return f"{x,y}"

if __name__ == "__main__":
    N = 5
    string = "RRRUDD"
    print(solution(N, string))