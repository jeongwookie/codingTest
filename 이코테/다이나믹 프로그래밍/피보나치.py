# memoization 하기 위한 리스트 초기화
dp = [0] * 100 # fibo(1)부터 fibo(99)까지 인덱스별로 저장

# top-down 으로 구현 : 시간복잡도가 O(N)으로 처리 가능
## 재귀적으로 구현하고, 마지막 종료조건을 명시함
def fibo(x):
    if x == 1 or x == 2: # 종료 조건 명시: fibo(1)과 fibo(2)는 둘 다 1임
        return 1

    if dp[x]: # dp에 값이 저장되어 있으면 (0이 아니면)
        return dp[x]

    dp[x] = fibo(x-1) + fibo(x-2) # fibo(x)의 값을 dp에 저장
    return dp[x]

# bottom-up 으로 구현
## 첫번째 조건들부터 시작해서 for문으로 하나씩 계산
def fibo_bottomup(x):
    dp[1], dp[2] = 1, 1
    for i in range(3, x+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[x]

# 결과 프린트
#print(fibo(99))
print(fibo_bottomup(99))

