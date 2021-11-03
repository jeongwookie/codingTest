def solution(iter, string):
    ans = ""
    for s in string:
        ans += s * iter

    return ans

if __name__ == "__main__":
    test_case = int(input())
    _list = []
    for _ in range(test_case):
        iter, string = input().split(" ")
        _list.append(solution(int(iter), string))

    # 출력
    for i in _list:
        print(i)
