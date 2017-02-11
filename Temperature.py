def main() :
    Temp = int(input("Enter temperature in Fahrenheit: "))
    Celsius = (Temp-32)*(5/9)
    print("Fahrenheit = ", Temp, ", Celsius = ", Celsius)
    reply = input("Want to continue? ")
    if reply.lower() == "yes" :
        main()
    elif reply.lower() == "no" :
        print("ok")
    else :
        print("I'll assume thats a yes.")
        main()
main()