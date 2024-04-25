a = int(input())
b = int(input())

alpha = a + b
sum = 0

for y in range(a - 1, -1, -1):
    for x in range(b):
        if (y == -(x-a+1)):
            print(sum, end = ' ')
            sum += alpha
        else:
            print("0",end = ' ')
    print("")
    
