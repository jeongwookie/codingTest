"""
종말의 수 : 어떤 수에 적어도 6이 연속으로 3개 들어간 수를 의미
666, 1666, 2666 과 같이 끝자리가 6인놈
6660, 6661, ... 과 같이 뒤에서 두번째 자리가 6인놈 (6666 있음 주의)
16660, 16662, ... , 96661, 96662, ...
66660, 66661, ...
이런 세밀한 조건들을 하나도 빠짐없이 짜야 완전탐색이 되는데 벌써부터 머리가 아픔;;
주어지는 숫자 N은 10000보다 작거나 같음. -> 그냥 통으로 돌려버리면 안되나? str matching으로.
"""
def solution(N):
    # N번 종말의 숫자를 generate한다.
    ## 걍 다 검사해서 뽑아버릴수 있을듯? N이 10000밖에 안되서.
    max_val = 10000000
    count = 0
    for i in range(max_val): # while True 로 걍 하면 될껄 왜 이렇게 했지? ㅋㅋ
        if "666" in str(i): # 이런식으로 666을 포함하는 놈 전부 차례대로 검사해서 뽑음.
            count += 1
            if count == N:
                ans = i
                break
    return ans

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    N = int(readline())
    print(solution(N))