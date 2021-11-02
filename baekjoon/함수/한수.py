"""
https://www.acmicpc.net/problem/1065
양의 정수 X의 각 자리가 등차수열을 이루는 수 = 한수
N이 주어졌을 때, 1보다 크거나 같고 N보다 작거나 같은 한수의 개수 출력하기.
"""
def is_han_number(number):
    str_number = str(number)
    if len(str_number) == 1:
        return True

    diff_list = []
    for i in range(len(str_number) - 1): # 998 -> 3
        diff = int(str_number[i + 1]) - int(str_number[i])
        if not diff_list:
            diff_list.append(diff)
        else:
            if diff_list[-1] == diff:
                diff_list.append(diff)
            else:
                return False

    return True

def solution(N):
    han_num_list = [i for i in range(1, N+1) if is_han_number(i)]
    return len(han_num_list)

if __name__ == "__main__":
    N = int(input())
    print(solution(N))

