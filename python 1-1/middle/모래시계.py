N = int(input())

for i in range(1,N+1):
    for space in range(N - i):
        print(" ",end = '')
    for ex in range(2*i - 1):
        print("X",end ='')
    print("")

for j in range(N - 1, 0, -1):
    for space in range(N - j):
        print(" ",end = '')
    for x in range(2*j - 1):
        print("X",end ='')
    print("")