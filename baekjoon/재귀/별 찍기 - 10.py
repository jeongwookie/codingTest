
### solution
size = int(input())
stars = [[' ' for i in range(size)] for _ in range(size)] # 좌표계 생성 [[' ' '],[' ' '],[' ' ']]

def fill_star(size, x, y):
    """
    미리 만들어놓은 좌표계에 별을 채우는 함수
    :param size: (size, size) 크기의 전체 좌표계
    :param x: 해당 좌표계 안에서 위치
    :param y: 해당 좌표계 안에서 위치
    :return:
    """
    if size == 1:
        stars[y][x] = '*'

    else: # size가 3, 9, 27 ...
        next_size = size // 3
        # 전체 좌표계를 크게 9개로 나눔.
        for dy in range(3):
            for dx in range(3):
                # 가장 가운데 (dx, dy) = (1,1) 을 제외하고 나머지를 next_size를 가진 star로 채운다.
                ## 주어진 좌표 (x, y) 를 시작점으로, next_size가 최소 단위로 곱해짐.
                if dx != 1 or dy != 1:
                    fill_star(next_size, x + dx * next_size, y + dy * next_size)

fill_star(size, 0, 0)
for i in stars:
    # y 좌표계가 동일한 x가 들어간 리스트안의 값들을 붙여서 출력
    print(''.join(i))
    #print(*i)