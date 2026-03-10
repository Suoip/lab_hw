try:
    sum = 0
    kWh_input = int(input('Input your electricity usage(kWh): '))
    if kWh_input <= 0:
        print('Your input cant be negative or zero.')
    if kWh_input <= 150 and kWh_input > 0:
        sum = kWh_input*1.5
        print(f'Your bill: {sum}')
    elif kWh_input > 150 and kWh_input <= 300:
        sum = (150*1.5) + ((kWh_input-150) * 2.2)
        print(f'Your bill: {sum}')
    elif kWh_input > 300:
        sum = (150*1.5) + 150*2.2 + (kWh_input-300) * 3.8
        print(f'Your bill: {sum}')
except ValueError as a:
    print(f'Your input is invalid, {a}')