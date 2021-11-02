"""
셀프 넘버 출력하기 : 생성자가 없는 숫자들
"""
def non_self_number_generator(number):
    return number + sum([int(i) for i in str(number)])

def self_number_list_generator(number):
    non_self_num_list = []
    for n in range(1, number):
        non_self_num = non_self_number_generator(n)
        non_self_num_list.append(non_self_num)

    non_self_num_list = sorted([i for i in set(non_self_num_list) if i <= number])
    self_num_list = [i for i in range(1, number) if i not in non_self_num_list]

    return self_num_list

if __name__ == "__main__":
    number = 10000
    for n in self_number_list_generator(number):
        print(n)


