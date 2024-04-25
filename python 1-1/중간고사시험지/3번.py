sum = ''

while(1):
    a = input()
    if a == ';':
        break
    if a == '?' or a == '!':
        continue
    elif a == 'u':
        n = int(input())
        for i in range(n):
            sum += '_'
    else:
        n = int(input())
        for j in range(n):
            sum += a

print(sum)


