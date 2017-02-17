from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

def main() :
    wordcount=[]
    count = 0

    f = askopenfilename()
    try :
        file = open(f, 'r')


        for word in file.read().split():
            wordcount.append(word)


        for i in range(len(wordcount)):
            j = wordcount[i]
            if 3 <= len(j) <= 8:
                count += 1
            i += 1

        sentences = open(f, 'r').read().count(".")
        average = count/len(wordcount)
        print(wordcount)
        print ('Average is {}'.format(average))
        print("Sentences: ", sentences)
        file.close()

    except:
        print("File error")
        ask = input("Try Again? Input yes or no: ")
        if ask.lower() == "yes":
            main()
        elif ask.lower() == 'no':
            print("Alright Baby, Miss you.")
        else:
            print('Say WhAAAAAAAAAAAAAT?')
            print('Try again B :')
            main()


main()









