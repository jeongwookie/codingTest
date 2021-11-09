def solution(discussion_time):
    """
    start, end 튜플이 주어질때, N개의 회의에 대해서 회의 안겹치게 배치
    사용할 수 있는 회의의 최대 갯수를 리턴
    그리디 알고리즘은 정당성 분석을 잘해야하는데..
    빨리 끝나는 순서대로 정렬해서 분석해본다. 회의가 빨리 끝날수록 뒤에 남은 시간이 많아서 회의 배치가 가능하기 때문.
    다만, 시작이 빠르면서 동시에 빨리 끝나야 하기 때문에,
    1차적으로 끝나는 시간으로 정렬 + 시작시간 오름차순 정렬을 수행한다.
    """
    # 두가지 기준으로 sort
    discussion_time = sorted(discussion_time, key=lambda x: (x[1], x[0]))
    #print(discussion_time)

    count = 1
    poped = discussion_time.pop(0)
    #ans = [poped]
    end = poped[1]

    for time in discussion_time:
        if time[0] >= end:
            end = time[1]
            count += 1
            #ans.append(time)
    #print(ans)
    return count

if __name__ == "__main__":
    import sys
    sys.stdin = open("../input.txt", "r")
    N = int(input())
    discussion_time = []
    for _ in range(N):
        start, end = map(int, input().split())
        discussion_time.append([start, end])

    print(solution(discussion_time))