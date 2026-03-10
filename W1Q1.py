current_year = 2026
try:
    x = str(input("Name: "))
    y = int(input("Birthyear: "))
    if y > current_year:
        print("Your input is invalid.")
        exit()
    z = str(input("Has your birthday passed this year?(yes/no) "))
except ValueError as _:
    print(f'Your input is invalid, {_}')
    exit()

else:
    if (z.lower() == 'yes'):
        print(f'You are {current_year - y} years old!')
    elif (z.lower() == 'no'):
        print(f'You are {current_year-y-1} years old!')
    else:
        print("Your input is invalid")
        exit()

