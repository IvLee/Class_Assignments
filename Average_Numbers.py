# array = list()
# Average = int(input("How many numbers do you want in a set? "))

# for i in range (Average) :
    # inputNr = int(input("Enter a number: "))
    # array.append(inputNr)

# print(array)
# print ("Average =", (sum(array)/Average))

def main() :
    b = int(input("number pls: "))
    sum = 0
    for i in range (0, b) :
        z = int(input("Enter a number "))
        print("Number %d is %d" % (i+1,z))
        sum = sum + z
    print ('The average is %d ' % (sum/b))

main()