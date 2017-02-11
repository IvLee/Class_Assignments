import time
def main() :
    print("Here's a chart of Celsius and Fahrenheit in increments of 5")
    print("Celsius             Fahrenheit")
    print("______________________________")

    for i in range (0,101,5) :
        print(i, "                     ", ((i*(9/5)+32)))
        time.sleep(0.5)

main()