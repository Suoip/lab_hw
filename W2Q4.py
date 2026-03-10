try:
    x = int(input('For mulpitlication:(1) For division:(2): '))
    y = float(input('Input the first num: '))
    z = float(input('Input the second num: '))

    if x == 1:
        print(f'Result: {y*x}')
    elif x == 2:
        print(f'Result: {y/z}')
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('Second input cant be zero')
    

