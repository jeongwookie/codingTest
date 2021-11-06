from itertools import combinations
import math

def solution(num_list, max_val):
    """
    주어진 숫자 M을 넘지 않으면서 N장의 카드 중 3장의 카드 고르기

    :return: 21과 가장 가까운 정수값 (3장 합)
    """

    # len(num_list) 개의 카드 중 3장을 중복을 허용하지 않는 조합으로 뽑기
    combination_list_of_cards = list(combinations(num_list, 3))
    #print(combination_list_of_cards)

    sum_list = sorted([sum(i) for i in combination_list_of_cards])
    sum_list = [i for i in sum_list if i <= max_val]

    return sum_list[-1]

if __name__ == "__main__":
    N, max_val = map(int, input().split())
    num_list = list(map(int, input().split()))
    print(solution(num_list, max_val))