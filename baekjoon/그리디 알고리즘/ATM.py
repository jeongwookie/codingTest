def solution(N, duration):
    """
    [3,1,4,3,2]
    기다리는 시간을 최소화 하면 그게 답 아닐까?
    => 뽑는데 시간이 젤 덜걸리는 사람부터 뽑으면 됨.
    """
    #1. _dict으로 각 사람별 기다리는 시간을 저장해둠
    _dict = {k:v for k,v in zip(range(1, N+1), duration)}

    #2. key를 value에 대해서 sort
    keys = sorted(_dict.keys(), key = lambda x: _dict[x])

    #3. total time 계산
    wait = 0
    ans = []
    for person in keys: # [1,2,3,3,4]
        wait += _dict[person]
        ans.append(wait)

    return sum(ans)

if __name__ == "__main__":
    import sys
    sys.stdin = open("../input.txt", "r")
    N = int(input())
    duration = list(map(int, input().split()))
    print(solution(N, duration))