N1 = int(input())
N2 = int(input())
N3 = int(input())

sum = N1 + N2 + N3

if sum % 12 == 0:
    print("%d is multiple of 3 and 4" %(sum))
elif sum % 3 == 0:
    print("%d is multiple of 3" %(sum))
elif sum % 4 == 0:
    print("%d is multiple of 4" %(sum))
else:
    print("%d is not multiple of 3 or 4" %(sum))