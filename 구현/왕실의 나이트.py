pos = input()

x_pos = int(ord(pos[0])-ord('a'))+1
y_pos = int(pos[1])

dir = [(2,1),(1,2),(-2,-1),(-1,-2),(2,-1),(1,-2),(-2,1),(-1,2)]
count = 0

for i in dir:
    nx = x_pos+i[0]
    ny = y_pos+i[1]
    
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)