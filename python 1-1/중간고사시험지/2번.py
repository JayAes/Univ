N1 = int(input())
N2 = int(input())

day = 0
hour = 0
minute = 0
second = 0

sum = N1 + N2
day = day + (sum // 86400)
sum = sum % 86400

hour = hour + (sum // 3600)
sum = sum % 3600

minute = minute + (sum // 60)
sum = sum % 60

second = sum

print("%d days %02d:%02d:%02d" %(day,hour,minute,second))