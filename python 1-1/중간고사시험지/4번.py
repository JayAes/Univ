N = int(input())

for i in range(N):
    result = 0
    
    year = int(input())
    major = input()
    num = int(input())
    
    year = year + 20
    
    if major == 'math':
        majornum = 1
    elif major == 'english':
        majornum = 2
    elif major == 'korean':
        majornum = 3

    print("%d%02d%02d" %(year,majornum,num))
    
