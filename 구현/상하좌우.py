N = int(input())
move_list = input().split()
dir = {"L":(0,-1),"R":(0,1),"U":(-1,0),"D":(1,0)}

x_pos = 1
y_pos = 1

for move in move_list:
    prv_x = x_pos
    prv_y = y_pos
    
    x_pos += dir[move][0]
    y_pos += dir[move][1]
    
    if x_pos < 1 or x_pos > N:
        x_pos = prv_x
    if y_pos < 1 or y_pos > N:
        y_pos = prv_y

print(x_pos, y_pos)