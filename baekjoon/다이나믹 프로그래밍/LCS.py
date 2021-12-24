if __name__ == "__main__":
    import sys; readline = sys.stdin.readline
    string_1 = ' ' + readline().rstrip() # 앞의 공백을 추가하여 index 0을 사용하지 않게끔 함
    string_2 = ' ' + readline().rstrip()

    # 최장 공통 부분 수열 구하기
    # LCS[i,j] : 문자열 1의 i번째 글자, 문자열 2의 j번째 글자까지의 LCS 길이 저장
    ## (i,j)번째 글자가 마지막인 LCS 길이 저장
    LCS = [[0] * (len(string_2)) for _ in range(len(string_1))] # 길이 0으로 초기화
    for i in range(1, len(string_1)):
        for j in range(1, len(string_2)):
            # string을 돌면서 같은 문자가 나오면, 바로 직전의 LCS값 + 1을 저장
            if string_1[i] == string_2[j]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            # 같은 문자가 아닌 경우
            ## 바로 직전의 LCS값을 보되, 각 string별로 확인함
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

    print(LCS[-1][-1])
