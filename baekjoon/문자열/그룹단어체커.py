def solution(word):
    """
    :param word:
    :return: boolean

    인풋의 word대하여, 존재하는 모든 char에 대해서 반드시 연속해서 나타나는 경우만을 말함.
    """
    answer = True

    #1. 들어온 단어에 대해서 set 처리해서 key를 골라냄
    chars_of_word = [i for i in set(word)]

    # 체커
    for c in chars_of_word:
        _list = [idx for idx, w in enumerate(word) if w == c] # word 안에 해당 char의 인덱스를 전부 뽑기.
        #print(f"index findall : {_list}")

        # 해당 idx 뽑은 리스트가 원소가 1개거나, 1개를 초과할 경우 인덱스의 차이가 반드시 1씩 나야한다..
        if len(_list) > 1:
            dist_list = list(set([j-i for i,j in zip(_list, _list[1:])])) # [1] , [1,2] , ...
            #print(f"distance 계산 : {dist_list}")

            # return 조건 정리
            if len(dist_list) == 1 and dist_list[0] == 1:
                pass
            else:
                answer = False
                break # false가 한번이라도 발생하면 그대로 종료

    return answer

if __name__=="__main__":
    answer = 0
    N = int(input())
    for _ in range(N):
        word = input()
        if solution(word):
            answer += 1

    print(answer)