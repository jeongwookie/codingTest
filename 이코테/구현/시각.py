"""
00시00분00초 부터 N시59분59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의수 리턴하기
A : 0~N (<=23)
B : 0~59
C : 0~59
전체 : (N+1) * 60 * 60
완전탐색 (Brute Force)으로 처리함. 총 경우의수가 24*60*60 밖에 안됨.
"""
def solution(N):
    count = 0
    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                _string = f"{h}{m}{s}"
                if "3" in _string:
                    count += 1

    return count

if __name__ == "__main__":
    N = 5
    print(solution(N))