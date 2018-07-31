
def wordlength():
    try:

        with open("File_to_be_counted.txt", "r") as inFile, open("outfile2.txt", "w") as outFile:

            eachWord = inFile.read().split()

            for word in eachWord:
                line = str(word+","+str(len(word))+"\n")
                outFile.write(line)


                # wordCount = {}
                # for word in inFile.read().split():
                #     if word not in wordCount:
                #         wordCount[word] = 1
                #     else:
                #         wordCount[word]+= word.__len__()
                # print(word,wordCount)
    except FileNotFoundError:
        print("Something went wrong. The file wasn't found")


wordlength()
