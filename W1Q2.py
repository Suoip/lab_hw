try:
    x = float(input("What is your height?(cm): "))
    y = float(input("What is your weight?(kg): "))
    print(f'Your BMI is: {(y/((x/100)**2)):.2f}')
except ZeroDivisionError as _:
    print(f"Your input is invalid, {_}")