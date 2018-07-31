# words can only contain the letters: a  b  d  e  i  l  m  n  o  t
#                                     6  1  7  4  3  2  9  8  0  5
# create an empty string called solvedWord we will add each found letter to
# create an array and fill it with num.
#
# loop through the array and if the position at i is equal to either a b d e i l m n o t, concatenate the given letter to
# the empty string (called solvedWord)
# when i = num.length then return solvedWord


def hidden(num):



    solvedWord = "" # empty string to store each letter when its solved

    numArray = [int(i) for i in str(num)] # create an array with each position at i being a digit of the hidden number

    for i in range(numArray.__len__()): # loop that runs for the length of the array and conditional statements compare
        if numArray[i] == 6:            # the values at i to the key and then concatenate to the solvedWord string
            solvedWord+=str("a")
        if numArray[i] == 1:
            solvedWord+=str("b")
        if numArray[i] == 7:
            solvedWord+=str("d")
        if numArray[i] == 4:
            solvedWord+=str("e")
        if numArray[i] == 3:
            solvedWord+=str("i")
        if numArray[i] == 2:
            solvedWord+=str("l")
        if numArray[i] == 9:
            solvedWord+=str("m")
        if numArray[i] == 8:
            solvedWord+=str("n")
        if numArray[i] == 0:
            solvedWord+=str("o")
        if numArray[i] == 5:
            solvedWord+=str("t")
    print(solvedWord)

hidden(637)                       # here are some example runs to show that it works
hidden(7468)
hidden(49632)
hidden(1425)
hidden(6250)
hidden(12674)
hidden(4735)








