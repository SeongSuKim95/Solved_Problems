N = int(input())

_datas = [list(map(int,input().split())) for _ in range(N**2)]
_dirlist = [[-1,0],[1,0],[0,-1],[0,1]]
_map = [[0]*N for _ in range(N)]


for idx,student in enumerate(_datas):

    if idx == 0 :
        _map[1][1] = student[0]
        continue
    else:
        num, friends = student[0], student[1:]
        coords = []
        for row in range(N):
            for col in range(N):
                if _map[row][col] == 0:
                    blank, friend = 0,0
                    for dir in _dirlist:
                        nrow,ncol = row + dir[0], col + dir[1]
                        
                        if nrow < 0 or nrow >=N or ncol < 0 or ncol >= N:
                            continue
                        
                        if _map[nrow][ncol] == 0 :
                            blank += 1

                        else :
                            if _map[nrow][ncol] in friends:
                                friend += 1
                    coords.append((friend,blank,row,col))
        coords.sort(key= lambda x : (-x[0],-x[1],x[2],x[3]))
        srow,scol = coords[0][2],coords[0][3]
        _map[srow][scol] = num

sum = 0
friend_score = {0:0,1:1,2:10,3:100,4:1000}
for row in range(N):
    for col in range(N):
       for data in _datas:
            if _map[row][col] == data[0]:
                friend = 0
                for dir in _dirlist:
                    nrow,ncol = row + dir[0], col + dir[1]
                    if nrow < 0 or nrow >=N or ncol < 0 or ncol >= N:
                        continue
                    if _map[nrow][ncol] in data[1:]:
                        friend +=1
                sum += friend_score[friend]

print(sum)