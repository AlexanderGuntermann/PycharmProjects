

def wordCounter():  # define function
    try:

        with open("File_to_be_counted.txt", "r") as inFile, open("output1.txt","w") as outFile:   # open the file in reading mode
            words = []  # list to save all the words
            word = ""
            for line in inFile:  # loop through every line in the file
                for word in line.split():  # split at every word and append the word to the list
                    words.append(word)


    except FileNotFoundError:
        print("Wrong file or path does not exist. Please make sure file exists or is named correctly")


wordCounter()
