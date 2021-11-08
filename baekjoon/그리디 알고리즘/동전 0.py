def solution(coin_value, K):
    """
    각각의 동전을 무한으로 가지고 있는 상태.
    동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 함.
    필요한 동전 개수의 최솟값을 리턴하라.
    -> K에 가장 가까운, 또는 K를 해당 벨류로 나누었을때 나누어떨어지는 동전 중 젤 큰걸로
    4200원 -> 각각의 벨류로 일단 다 나눠봄.
    몫이 0이면 -> 아예 해당사항이 없음.
    그냥 이거를 N보다 큰놈이라고 하고 다 짤라내도됨.
    몫이 1 이상인 애들로만 구성해야함.
    그중에 젤큰넘 1000으로 나누면 몫이 4고 나머지가 200원
    200원에 대해서 또 얘보다 크거나 같은 벨류 중 제일 큰애로 나눠줌. 100이니까 몫이 2고 나머지 0
    => 총합 6
    """
    coin_value = sorted([i for i in coin_value if i <= K], reverse=True) # 1000,50,10,5
    count = 0
    for coin in coin_value:
        if coin > K:
            continue

        Q = K // coin
        R = K % coin

        # update
        count += Q
        if R == 0:
            break
        else:
            K = R

    return count

if __name__ == "__main__":
    import sys
    sys.stdin = open("../input.txt", "r")
    N, K = map(int, input().split())
    coin_value = []
    for _ in range(N):
        coin_value.append(int(input()))

    print(solution(coin_value, K))