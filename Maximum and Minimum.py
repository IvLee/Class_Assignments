def main() :
    array = list()

    def elements():
        try:
            average = int(input("How many elements do you want for the array? "))
            for i in range(average):
                num = int(input("Enter the numbers for the array: "))
                array.append(num)
            print(array)
        except:
            print('Invalid input, start again. ')
            elements()


    def max():
        mx = 0
        for i in range(len(array)):
            if array[i] > mx:
                mx = array[i]
        print('Max: {}'.format(mx))

    def min():
        mn = array[0]
        for i in range(len(array)):
            if array[i] <= mn:
                mn = array[i]
        print('Min: {}'.format(mn))

    elements()
    max()
    min()

main()

