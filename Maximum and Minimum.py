def main() :
    array = list()
    try:
        average = int(input("How many elements do you want for the array? "))
    except:
        print('Invalid input, please input a number: ')
        main()

    def elements():
        for i in range (average) :
            try:
                num = int(input("Enter the numbers for the array: "))
                array.append(num)
            except ValueError:
                print('Invalid input, please input a number: ')
                elements()
        print(array)
    elements()

    for i in range(len(array)):



main()

