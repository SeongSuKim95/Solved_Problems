N,M,x,y,C = map(int,input().split())

map_list = []
command = []
for i in range(N):
     map_list.append(list(map(int,input().split())))

# print(map_list)
command = list(map(int,input().split()))
dice =[
    [2,0,5,3,4,1],
    [1,5,0,3,4,2],
    [4,1,2,0,5,3],
    [3,1,2,5,0,4]
]
# 바닥

dir_x = [0,0,-1,1]
dir_y = [1,-1,0,0]
dice_list, temp = [0] * 6, [0] * 6

for i in command:
    x, y = x + dir_x[i-1], y + dir_y[i-1]
    if x<0 or x>=N or y <0 or y>=M:
        x,y = x - dir_x[i-1], y - dir_y[i-1]
        continue

    for idx in range(6):
        temp[idx] = dice_list[idx]
    for idx in range(6):
        dice_list[idx] = temp[dice[i-1][idx]]
    if map_list[x][y] != 0 :
        dice_list[5] = map_list[x][y]
        map_list[x][y] = 0
    else :
        map_list[x][y] = dice_list[5]
    print(dice_list[0])