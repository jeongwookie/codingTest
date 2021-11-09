def solution(discussion_time):
    """
    sort를 두번하면 시간이 너무 오래 걸림.
    end 기준으로 정렬할꺼니까, 아예 리스트를 만들때 서로 자리를 바꿔서 넣는다.
    discussion_time : [[end,start],[],[],...] 순으로.
    흠 이거는 그냥 테크닉이었던걸로.
    실상은 백준의 인풋 문제였음. input = sys.stdin.readline 하면 해결됨.
    """
    # sort
    discussion_time = sorted(discussion_time)
    #print(discussion_time)

    count = 0
    end = 0
    ans = []
    for curr_end, curr_start in discussion_time:
        if curr_start >= end:
            end = curr_end # update
            count += 1
            #ans.append([curr_start, curr_end])

    #print(ans)
    return count

if __name__ == "__main__":
    import sys
    sys.stdin = open("../input.txt", "r")
    N = int(input())
    discussion_time = []
    for _ in range(N):
        start, end = map(int, input().split())
        discussion_time.append([end, start]) # 둘의 자리를 바꿔서 넣음

    print(solution(discussion_time))