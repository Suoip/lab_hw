try:
    n = int(input('Input n: '))
    for x in range(1,n+1):
        for y in range(1,n+1):
            print(x*y, end=' ')
        print('',end='\n')
except:
    print('Invalid input.')