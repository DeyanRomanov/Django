n = int(input())

if not n % 2 == 0:
    print('Weird')
else:
    if 1 < n < 6:
        print('Not Weird')
    elif 5 < n <= 20:
        print('Weird')
    else:
        print('Not Weird')
