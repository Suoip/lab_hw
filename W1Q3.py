x = int(input("Result of first exam(0-100): "))
if not ((x >= 0) and (x <= 100)):
    print('Invalid, not in range.')
    exit()
y = int(input("Result of second exam(0-100): "))
if not ((y >= 0) and (y <= 100)):
    print('Invalid, not in range.')
    exit()
z = int(input("Result of third exam(0-100): "))
if not ((z >= 0) and (z <= 100)):
    print('Invalid, not in range.')
    exit()
print(f'Result average: {(x+y+z)/3}')