year1 = int(input())
year2 = int(input())
month1 = int(input())
month2 = int(input())
day = int(input())

j = month1

for i in range(year1,year2+1):
    while(1):
        j += 1
        if (j == 13):
            j = 1
            break
        if (j == month2+1):
            break
        for d in range(1,day+1):
            if (j % 2 == 0):
                if d == 31:
                    break
            print("%04d/%02d/%02d" % (i,j,d))


