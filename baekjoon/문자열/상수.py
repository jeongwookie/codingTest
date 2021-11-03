def solution(first, second):
    first, second = int(str(first)[::-1]), int(str(second)[::-1])
    return max(first, second)

if __name__ == "__main__":
    first, second = map(int, input().split())
    print(solution(first, second))