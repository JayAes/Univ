N = int(input())

for s in range(N):
    for y in range(N - 1, -1, -1):
        for k in range(N):
            for x in range(N):
                if (y >= x - (N-1)/2) and (y - N + 1 <= x - (N-1)/2) and (y >= -x + (N-1)/2) and (y - N + 1 <= -x +(N -1)/2):
                    print("X",end = '')
                else:
                    print(" ",end = '')
        print("")
        
## 세로는 N - 1이다.
## 가로는 N - 1이다.