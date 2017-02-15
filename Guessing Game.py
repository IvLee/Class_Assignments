import random

attempts = 3
secret_number = random.randint(1, 10)

try :
    for attempt in range(attempts):

        guess = float(input('Take a guess: '))

        if guess == (secret_number-1) or guess == (secret_number+1):
                    print('Hot')
        elif guess == (secret_number-2) or guess == (secret_number+2):
                    print('Warm')
        else:
            print()
            print('You guessed it! The number was', secret_number)
            print('You guessed it in', attempts, 'attempts')

        print('Sorry you reached the maximum number of tries')
        print('The secret number was', secret_number)
except :
    print("Error")