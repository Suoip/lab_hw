from random import randint
try:
    b = int(input("Input a digit: "))
    y = int(input('Declare guess limit: '))
    x = randint(1,b)


    def main():
        a = 0
        while a < y:
            a += 1
            guess = int(input("Input a guess: "))
            if guess == x:
                print(f'Congrats! You found it in {a} guess(es)')
                break
            elif a == y:
                print("You ran out of guesses")
                break
            elif guess < x:
                print(f'Your guess is lower.')
            elif guess > x:
                print(f'Your guess is higher.')
    main()
except:
    print('Invalid input.')