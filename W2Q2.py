import re

def is_valid_pswdr(i):
    pattern = r'^(?=[A-Za-z\d]{9}$)(?=[^0-9]*\d[^0-9]*$)[A-Za-z]{0,8}\d?[A-Za-z]*$'
    if re.match(pattern, i):
        print('Valid Password')
    else:
        print('Invalid Password')

pswrd = str(input('Input a password containing 8 letters and 1 digit: '))
is_valid_pswdr(pswrd)