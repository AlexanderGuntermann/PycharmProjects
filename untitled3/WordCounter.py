from collections import Counter

def wordCounter():  # define function
    try:
            # open both files, one as input to read data and the second to output and write data
         with open("File_to_be_counted.txt", "r") as inFile, open("outfile1.txt","w") as outFile:

            # singleWords = {}
            # Counter method that takes each word split from the inFile as an argument and keeps track of it
            wordcount = Counter(inFile.read().split())


            # for word in inFile.read().split():  # loop through every line in the file and split by each space
            #     if word not in singleWords:  # if the word doesn't exist, value = 0
            #         singleWords[word] == 1
            #     else:
            #         singleWords[word] += 1 # else the word exists and increment the counter by 1

            # for every item in wordcount, print them out alongside their frequency. This also writes the information to
            # the outfile.
            for item in wordcount.items():
                print("{}\t{}".format(*item))
                outFile.write("{}\t{}".format(*item)+"\n")


    except FileNotFoundError:
        print("Wrong file or path does not exist. Please make sure file exists or is named correctly")


wordCounter()
