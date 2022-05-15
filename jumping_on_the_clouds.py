def jumpingOnClouds(c):
    c = list(map(int, c))
    indx = 0
    step = 0
    while c:
        if indx + 2 < len(c) and c[indx + 2] == 0:
            step += 1
            c = c[(indx+2):]
        elif indx + 1 < len(c) and c[indx + 1] == 0:
            step += 1
            c = c[(indx+1):]
        else:
            break
    return step


c = input().split()
result = jumpingOnClouds(c)
print(result)