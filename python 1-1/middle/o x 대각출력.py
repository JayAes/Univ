N = int(input())

for y in range(N -1, -1, -1):
    for x in range(N):
        if y == x or y == -(x-N+1):
            print(" X",end ='')
        else:
            print(" O",end = '')
    print("")