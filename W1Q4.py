try:
    x = int(input('Input the amount of minutes you want in Hour.Minute format: '))
    print(f'Hour.Minute format: {x // 60 }.{x % 60}')
except ValueError as _:
    print(f'Your input is invalid, {_}')