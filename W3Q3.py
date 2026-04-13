try:
    data = []
    x = int(input('Input data, input (-1) to end.'))
    while x != -1:
        data.append(x)
        x = int(input('Input data, input (-1) to end.'))

    min = data[0]
    max = data[0]
    for num in data:
        if num < min:
            min = num

    for num in data:
        if num > max:
            max = num

    print(f'Count: {len(data)} \n Sum: {sum(data)} \n Min: {min} \n Max: {max}')
except IndexError:
    print("You haven't inputed anything")
except:
    print('Invalid input')