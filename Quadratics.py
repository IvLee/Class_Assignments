import time
print("Welcome!!")
time.sleep(2)
print("Let's do a bit of math, shall we?")
time.sleep(2)

def  quadratic ():
    print("Please input values for the quadratic formula : Ax\u00b2+Bx+C")
    time.sleep(2)
    try :
        a = int(input("What is your value of A? "))
    except ValueError :
        time.sleep(1)
        print("Come on, this is math not English. Give me a number!")
        quadratic()
    try :
        b = int(input("What is your value of B? "))
    except ValueError :
        time.sleep(1)
        print("Made a mistake? Try again...")
        quadratic()
    try :
        c = int(input("What is your value of C? "))
    except ValueError :
        time.sleep(2)
        print("Please be serious about this.. you were almost there..")
        quadratic()
    try :
        d = int(input("What is your value of X? "))
    except ValueError :
        time.sleep(4)
        print("You just had to mess this up, huh!? You know what? NO MATH FOR YOU!")
        exit()
    else :
        print('{}({:-})^2{:+}({:-}){:+} = '.format(a,d,b,d,c), ((a*(d**2))+(b*d)+c))
        time.sleep(2)
        ask()

def ask () :
    answer = input("Want to do another one? ")
    if answer.lower() == "yes":
        quadratic()
    elif answer.lower() == "no":
        exit()
    else :
        print("I'm sorry, can you repeat that?")
        time.sleep(1)
        ask()

quadratic()
