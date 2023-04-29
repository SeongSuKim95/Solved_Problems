BOARD_NUM = 2

# 변수 선언 및 입력:

# 3가지 타일 모양을 지정합니다.
shapes = [
    [],

    [[1, 0],
     [0, 0]],

    [[1, 1],
     [0, 0]],

    [[1, 0],
     [1, 0]],
]

n, m, k = 6, 4, int(input())

board = [
    [
        [0 for _ in range(m)]
        for _ in range(n)
    ]
    for _ in range(BOARD_NUM)
]

score = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


def can_go(b_num, tile_type, x, y):
    # 바닥에 부딪히거나, 벽돌이 존재하는 경우에는
    # 진행이 불가합니다.
    for dx in range(2):
        for dy in range(2):
            if shapes[tile_type][dx][dy]:
                nx, ny = x + dx, y + dy
                
                if not in_range(nx, ny) or \
                   board[b_num][nx][ny]:
                    return False
                
    return True


def put(b_num, tile_type, x, y):
    for dx in range(2):
        for dy in range(2):
            if shapes[tile_type][dx][dy]:
                nx, ny = x + dx, y + dy
                board[b_num][nx][ny] = 1
            

def all_filled(b_num, row):
    return all([
        board[b_num][row][col] == 1
        for col in range(m)
    ])


def down_one_line(b_num, end_row):
    for row in range(end_row, 0, -1):
        for col in range(m):
            board[b_num][row][col] = board[b_num][row - 1][col]
            board[b_num][row - 1][col] = 0


def process_dark(b_num):
    global score
    
    # 아래에서 위 방향으로 줄 마다
    # 가득 채워져 있는지 확인하여
    # 그 경우에는 점수에 1을 더해주고 
    # 한 줄씩 당겨줍니다.
    row = n - 1
    while(row >= 2):
        if all_filled(b_num, row):
            score += 1
            down_one_line(b_num, row)
        else:
            row -= 1
    

def block_exist(b_num, row):
    return any([
        board[b_num][row][col] == 1
        for col in range(m)
    ])


def process_light(b_num):
    # Step1. 첫 번째 행, 두 번째 행 중
    # 블럭이 한 개라도 놓여있는 행의 수를 셉니다.
    
    drop_cnt = 0
    if block_exist(b_num, 0):
        drop_cnt += 1
    if block_exist(b_num, 1):
        drop_cnt += 1
    
    # Step2.
    # 해당 수 만큼 타일을 한 줄씩 내려줍니다.
    for _ in range(drop_cnt):
        down_one_line(b_num, n - 1)


def drop(b_num, tile_type, col):
    # Step1. 블럭을 떨어뜨립니다.
    for row in range(n):
        # 그 다음 행으로 진행할 수 없다면
        # 블럭을 안착시킵니다.
        if not can_go(b_num, tile_type, row + 1, col):
            put(b_num, tile_type, row, col)
            break
    
    # Step2. 진한 부분에 대한 처리를 진행합니다.
    process_dark(b_num)
    
    # Step3. 연한 부분에 대한 처리를 진행합니다.
    process_light(b_num)


def simulate(t, x, y):
    # Step1. 노란색 영역에서 진행합니다.
    drop(0, t, y)
    
    # Step2. 빨간색 영역에서 진행합니다.
    # 이는 그림에서 빨간색 영역을 
    # 시계방향으로 90' 회전하여
    # 노란색 영역에서와 같이 진행하면 됩니다.
    # 각각의 블럭 type에 대해 
    # 떨어지는 위치 선정이 중요합니다.
    if t == 1:
        drop(1, 1, m - 1 - x)
    elif t == 2:
        drop(1, 3, m - 1 - x)
    else:
        drop(1, 2, m - 1 - (x + 1))


def remaining_num():
    return sum([
        board[l][i][j]
        for l in range(2)
        for i in range(n)
        for j in range(m)
    ])


# k번 시뮬레이션을 반복합니다.
for _ in range(k):
    t, x, y = tuple(map(int, input().split()))
    simulate(t, x, y)

print(score)
print(remaining_num())