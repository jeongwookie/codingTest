def solution(string):
    croatia_alphabet_group1 = ["c=", "c-", "d-", "s=", "z="]
    croatia_alphabet_group2 = ["dz=", "lj", "nj"] # dz, lj, nj는 무조건 1글자로 봄

    # string : dz=ak 일때, d z= 가 아니고 dz= 가 우선되어야함.
    ## 체크 완료한 애는 제거해준다.
    string_copied = string
    for word in croatia_alphabet_group2:
        if word in string_copied:
            string_copied = string_copied.replace(word, '@')

    for word in croatia_alphabet_group1:
        if word in string_copied:
            string_copied = string_copied.replace(word, '@')

    # 리턴
    return len(string_copied)

if __name__ == "__main__":
    string = input()
    print(solution(string))