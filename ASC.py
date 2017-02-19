from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os, os.path

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
            if 3 <= len(j) <= 5:
                count += 1
            i += 1

        psentences = open(f, 'r').read().count(".")
        csentences = open(f, 'r').read().count( ",")
        semcolpsentences = open(f, 'r').read().count(";")
        expsentences = open(f, 'r').read().count('!')
        qsentences = open(f, 'r').read().count('?')
        colpsentences = open(f, 'r').read().count(":")
        sentences = psentences + csentences + colpsentences + expsentences + semcolpsentences + qsentences
        average = count/len(wordcount)
        #print(wordcount)
        print ('Average words is {}'.format(average))
        print("Sentences: ", sentences)
        file.close()
        savetext(average,sentences, f)

        ask = input("Want to choose another file? Input yes or no: ")
        if ask.lower() == "yes":
            main()
        elif ask.lower() == 'no':
            print("Alright Baby, Miss you.")
        else:
            print('Say WhAAAAAAAAAAAAAT?')
            print('Try again B :')
            main()


    except:
        print("File not found error")
        ask = input("Try Again? Input yes or no: ")
        if ask.lower() == "yes":
            main()
        elif ask.lower() == 'no':
            print("Alright Baby, Miss you.")
        else:
            print('Say WhAAAAAAAAAAAAAT?')
            print('Try again B :')
            main()

def savetext(a, b,c):
    prof_path = os.environ['USERPROFILE']
    text = input('Do you want to save results to a text file? ')
    if text.lower() == 'yes':
        name = input('Please enter a name for your results: ')
        filename = os.path.join(prof_path, 'Desktop', '{}.txt'.format(name))
        with open(filename, 'w') as f:
            f.write('Here are the average word results for {}'.format(c))
            f.write('\nAverage words is {}'.format(a))
            f.write("\nSentences: {}".format(b))
    elif text.lower() == 'no':
        print('Alright, Goodbye.')
    else:
        print('Please try again.')
        savetext(a,b)


main()









