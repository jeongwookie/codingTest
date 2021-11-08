# 제일 아래 원판을 3번 스택으로 옮기는 step
## 옮기고 나면 자동으로 f(N-1)이 됨.

# step1. 제일 아래 원판을 제외한 모든 원판을 stack_2에다가 순서대로 쌓기
# step2. 제일 아래 원판을 stack_3에다가 쌓기
# step3. step1에서 완성한 tower(N-1)을 진행하기

class HanoiTower:
    def __init__(self, N):
        # 원판 셋팅
        self.stack_1 = [i for i in range(1, N+1)][::-1]
        self.stack_2 = []
        self.stack_3 = []
        self.structure_dict = {1 : self.stack_1, 2: self.stack_2, 3: self.stack_3}
        self.count = 0 # 이동 횟수 저장소

    def move(self, _from, _to):
        print(f"move 전 상태 - stack_{_from} : {self.structure_dict[_from]}, stack_{_to} : {self.structure_dict[_to]}")
        if len(self.structure_dict[_from]) == 0:
            print("옮기기를 지정한 스택이 비었습니다. move 되지 않습니다.")
            return False

        if len(self.structure_dict[_to]) == 0: # 비어있으면,
            poped = self.structure_dict[_from].pop(-1)
            self.structure_dict[_to].append(poped)

        elif self.structure_dict[_from][-1] >= self.structure_dict[_to][-1]:
            print("옮기기를 지정한 원판의 크기가 너무 큽니다. move 되지 않습니다.")
            return False

        else: # to가 비어있지 않고, 정상적인 경우
            poped = self.structure_dict[_from].pop(-1)
            self.structure_dict[_to].append(poped)

        print(f"move 후 상태 - stack_{_from} : {self.structure_dict[_from]}, stack_{_to} : {self.structure_dict[_to]}")
        self.count += 1
        #print(f"answer : {_from} {_to}")
        return True

    def __repr__(self):
        return f"하노이탑 상태 - stack_1 : {self.stack_1}, stack_2 : {self.stack_2}, stack_3 : {self.stack_3}\n이동 횟수 - {self.count}"


# N이 짝수인가 홀수인가에 따라서 다른듯?
def solution(num_of_plate):
    hanoi_tower = HanoiTower(num_of_plate)
    print(hanoi_tower)

    if num_of_plate == 1:
        hanoi_tower.move(1, 3)
        return 1

    if num_of_plate == 2:
        # step1
        hanoi_tower.move(1, 2)
        # step2 : stack_1에 남은 원소가 단 1개일때. 최대값일때.
        hanoi_tower.move(1, 3)
        # step3 : n-1번째와 동일. 근데 횟수는 똑같은데 위치 셋팅이 다름 ㅠ ㅅㅂ


    if num_of_plate % 2 == 1: # 홀수, 3일때
        ## step1
        hanoi_tower.move(1, 3)
        hanoi_tower.move(1, 2)
        hanoi_tower.move(3, 2)
        ## step2
        hanoi_tower.move(1,3)
        ## step3
        print(hanoi_tower)

    else: # 짝수, 4일때
        ## step1
        hanoi_tower.move(1, 2)
        hanoi_tower.move(1, 3)
        hanoi_tower.move(2, 3)
        hanoi_tower.move(1, 2)
        hanoi_tower.move(3, 1)
        hanoi_tower.move(3, 2)
        hanoi_tower.move(1, 2)
        ## step2
        hanoi_tower.move(1, 3)
        ## step3
        print(hanoi_tower)

num_of_plate = 4