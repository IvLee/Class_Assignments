import time
print("Welcome!!")
time.sleep(2)
print("Let's do a bit of math, shall we?")
time.sleep(2)

def  quadratic ():
    print("Please input values for the quadratic formula : Ax\u00b2+Bx+C")
    time.sleep(2)
    a = int(input("What is your value of A?"))
    b = int(input("What is your value of B?"))
    c = int(input("What is your value of C?"))
    d = int(input("What is your value of X?"))
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
