N = int(input())
win = 0
draw = 0
lose = 0

for i in range(N):
    
    a = str(input())
    b = str(input())
    
    if (a == 's' or a == 'S'):
        if (b == 'S' or b == 's'):
            draw += 1
        elif (b == 'r' or b == 'R'):
            lose += 1
        else:
            win += 1
    elif (a == 'R' or a == 'r'):
        if (b == 'R' or b == 'r'):
            draw += 1
        elif (b == 'p' or b == 'P'):
            lose += 1
        else:
            win += 1
    else:
        if (b == 'p' or b == 'P'):
            draw += 1
        elif (b == 's' or b =='S'):
            lose += 1
        else:
            win += 1

print("Win:",win)
print("Draw:",draw)
print("Lose:",lose)