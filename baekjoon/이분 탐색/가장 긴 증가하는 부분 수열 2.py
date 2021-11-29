"""
대단히 유명한 문제. 조건에 따라서 DP로도 풀 수 있음.
bisect_left는 정렬된 리스트에서 target을 insert 할 때의 위치를 리턴함

"""
if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    from bisect import bisect_left
    N = int(readline().strip())
    array = list(map(int, readline().split()))
    stack = [array[0]] # 증가하는 부분 수열 저장소

    for num in array: # O(N)
        if stack[-1] < num: # 증가하는 부분이니까 제일 뒤에 붙이기
            stack.append(num)
        else:
            # 같거나 작을 경우, 이분 탐색으로 위치를 확인한 후 넣어준다.
            stack[bisect_left(stack, num)] = num
    #print(stack)
    print(len(stack))




