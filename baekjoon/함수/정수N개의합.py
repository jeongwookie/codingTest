#import sys
#sys.stdin = open("../input.txt", "r")

def solve(a: list) -> int:
    return sum(a)

if __name__ == "__main__":
    _list = [1,2,3]
    print(solve(_list))