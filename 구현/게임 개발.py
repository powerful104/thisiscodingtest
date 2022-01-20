N, M = list(map(int, input().split()))
A, B, d = list(map(int, input().split()))
map_info = []

#맵 구성
for _ in range(N):
    map_info.append(list(map(int, input().split())))

map_check = list(map_info)

dir_num = [0,1,2,3]
dir = [(-1,0),(0,1),(1,0),(0,-1)]

count = 1
nomove = 0

while True:
    d = dir_num[d-1]
    na = A + dir[d][0]
    nb = B + dir[d][1]
    
    if map_check[na][nb] == 0:
        A = na
        B = nb
        nomove = 0
        map_check[na][nb] = 1
        count += 1
    else:
        nomove += 1
    
    if nomove == 4:
        na = A - dir[d][0]
        na = B - dir[d][1]
        if map_info[na][nb] == 1:
            break
print(count)