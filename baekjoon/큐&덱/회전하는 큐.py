"""
# Contain 1, 2, 3, 4, 5 in deq
deq = deque([1, 2, 3, 4, 5])

deq.rotate(1) => 양수를 주면 우측으로 한칸 이동함
print(deq)
# deque([5, 1, 2, 3, 4])

deq.rotate(-1) => 음수를 주면 좌측으로 한칸 이동함
print(deq)
# deque([1, 2, 3, 4, 5])
"""
if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from collections import deque
    N, M = map(int, readline().split())
    targets = list(map(int, readline().split())) # 타겟 위치, 1부터 시작
    queue = deque([i for i in range(1, N+1)])

    # 주어진 순서대로 뽑아내기
    # 시작 위치에서 dist를 좌우로 계산해야함. 그래야 왼쪽으로 돌지 오른쪽으로 돌지 판단 가능
    count = 0
    for target in targets:
        right_dist = queue.index(target) # 1 - 0 = 1
        left_dist = len(queue) - queue.index(target) # 10 - 1 = 9
        if right_dist <= left_dist: # 오른쪽 거리가 짧을 경우, 왼쪽으로 칸 이동을 진행함
            queue.rotate(-right_dist)
            count += right_dist
        else: # 왼쪽 거리가 짧을 경우, 오른쪽으로 칸 이동을 진행함
            queue.rotate(left_dist)
            count += left_dist
        queue.popleft() # 제일 앞 숫지가 target이므로 pop 해줌

    # return
    print(count)




