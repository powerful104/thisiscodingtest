N, M = list(map(int, input().split()))
A, B, d = list(map(int, input().split()))
map_info = []

#맵 구성
map_info.append([0]*M)
for _ in range(N):
    map_info.append([0]+list(map(int, input().split()))+[0])
map_info.append([0]*M)


dir_num = [0,1,2,3]
dir = [(-1,0),(0,1),(1,0),(0,-1)]

count = 0
nomove = 0

while True:
    nd = dir_num[d-1]
    na = A + dir[nd][0]
    nb = B + dir[nd][1]
    
    if map_info[na][nb] == 1:
        A = na
        B = nb
        nomove = 0
    else:
        nomove += 1
    
    d = dir_num[d-1]