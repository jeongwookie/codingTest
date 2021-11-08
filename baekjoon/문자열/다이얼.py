def solution(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    _dict = {}
    iter = 0 # 총 8번 가능함. 그러니까 7
    idx = 0
    while iter < 8:
        if iter not in [5,7]:
            alphabet_sliced = alphabet[idx: idx+3]
            idx += 3
        elif iter == 7:
            alphabet_sliced = alphabet[idx:]
        else: # iter == 5
            alphabet_sliced = alphabet[idx: idx+4]
            idx += 4

        for c in alphabet_sliced:
            _dict[c] = (iter+2) + 1 # 해당 char을 누를때 걸리는 시간을 저장함
        iter += 1

    # 리턴 계산
    _list = [_dict.get(i) for i in string]
    return sum(_list)

if __name__ == "__main__":
    string = input()
    print(solution(string))