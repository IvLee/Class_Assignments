import time
time.sleep(2)
print("Why hellooooooooooooooo there!")
time.sleep(1)
print("Welcome to Supercalifragilisticexpialidocious!")
time.sleep(2)
print("The Land of weird stuff!")
time.sleep(2)

name = input("What is your name little one? ")
time.sleep(2)
print("Nice to meet you, " + name + "!")
time.sleep(1)
print("It's weird that we met! Dont you think that's weird????")
time.sleep(3)

color = input("Btw, What is your favorite color " + name + "? ")
time.sleep(2)
print("Oh! " + color + "?")
time.sleep(2)
print("...")
time.sleep(3)
print("My color personality horoscope says that you are retarded..")
time.sleep(2)
print("Now it's weird that you are retarded. I'm retarded too!")
time.sleep(2)

food = input("What's your favorite food? ")
time.sleep(2)
print(food + " awesome!!")
time.sleep(2)

def ask():
    leave = input("Do you need to leave? ")
    if leave.lower() == "no" :
       ask()

    elif leave.lower() == "yes":
        print("I am sooooo lonely! T_T Don't leave me!")

    else :
        print("huh??????")
        ask()
ask()





