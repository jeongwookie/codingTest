def solution(num):
    num_str = str(num)
    return sum([int(i) for i in num_str])

if __name__ == "__main__":
    N = input()
    number = input()
    print(solution(number))