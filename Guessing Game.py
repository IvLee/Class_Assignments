import random
import time

print("Welcome to the Guessing Game!")
time.sleep(1)
print("You only have 3 attempts!")
time.sleep(1)

def ask():
    ask = input('Want to try again? ')
    if ask.lower() == "yes":
        game()
    else:
        print('OK, Goodbye!')

def game():
    attempts = 3
    secret_number = random.randint(1, 10)
    print (secret_number)
    try :
        for attempt in range(attempts):
            print('This is attempt {}!'.format(attempt+1))
            time.sleep(1)
            guess = int(input('Take a guess between 1-10: '))

            if guess > 10 or guess < 1:
                print('OUT OF BOUNDS!!!!')
                print('Cold, Cold, Freezing COLD!')
                print('Game Reset.')
                game()

            elif guess == (secret_number-1) or guess == (secret_number+1):
                print('Hot')
            elif guess == (secret_number-2) or guess == (secret_number+2):
                print('Warm')
            elif guess < (secret_number-2) or guess > (secret_number+2) :
                print('Cold')

            elif guess == secret_number:
                print('Congrats on choosing the correct answer!!!')
                time.sleep(1)
                print('You did this in {} tries!'.format(attempt+1))
                time.sleep(1)
                print('Brag to all of your friends!')
                ask()

        print('Too Bad! You went over the max amount of attempts!')
        print('Better luck next time!')
        ask()



    except :
        print("Error")
        time.sleep(1)
        print('Game Reset.')
        time.sleep(1)
        game()

game()
ask()


