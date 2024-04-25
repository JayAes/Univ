wakehour = int(input())
wakeminute = int(input())
carrotmin = int(input())
carrotneed = int(input())

carrotcount = 0


i = 1
while(1):
    if carrotcount == carrotneed:
        break
    elif i == 1 and wakehour < 22:
        currenthour = wakehour
        currentminute = wakeminute
        print("%02d:%02d Carrot Time!" %(currenthour, currentminute))
        carrotcount += 1
        i += 1
    elif wakehour > 22:
        break
    else:
        currenthour += carrotmin // 60
        currentminute += carrotmin % 60
        
        if currentminute >= 60:
            currenthour += currentminute // 60
            currentminute %= 60
        
        if currenthour >= 22:
            break
            
        print("%02d:%02d Carrot Time!" %(currenthour, currentminute))
        carrotcount += 1

if carrotcount < carrotneed:
    print("Emergency!")
    