def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    x, y = map(int, readline().split())
    print(gcd(x, y))
    print(lcm(x, y))