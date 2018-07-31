

def wordCounter():  # define function
    try:

        with open("File_to_be_counted.txt", "r") as inFile, open("output1.txt","w") as outFile:   # open the file in reading mode
            wordFrequency = {}  # dict to save all the words
            singleWord = inFile.split()

            for singleWord in wordFrequency:
                if singleWord not in wordFrequency:
                    wordFrequency[singleWord] = 0
                else:
                    wordFrequency[singleWord] += 1

        for singleWord in wordFrequency:
            print(singleWord,wordFrequency)

    except FileNotFoundError:
        print("Wrong file or path does not exist. Please make sure file exists or is named correctly")


wordCounter()
