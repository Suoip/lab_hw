try:
    prev = None
    current_count = 0
    max_count = 0

    while True:
        num = int(input('Input a number: '))

        if num < 0:
            break
        if prev is not None:
            if num > prev:
                current_count += 1
            else:
                current_count = 0
            if current_count > max_count:
                max_count = current_count
        prev = num
    print(f'Max amount of times where it increased: {max_count+1}')

except:
    print('Invalid input.')