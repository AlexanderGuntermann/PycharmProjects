import pprint
import copy


def postman():
    # prompt user for rows
    inputRows = int(input("Please input the number of rows: "))
    # prompt user for columns
    inputCols = int(input("Please input the number of cols: "))
    # start the loop at 1 because row 0 is all 'c'


    # create a 2 dimensional matrix with the size rows by cols. Filled entire matrix with 'c' for closed
    matrix = [['c' for x in range(inputRows)] for y in range(inputCols)]
    listTwo = []
    # loop through first dimension for rows
    for i in range(inputRows):
        # first iteration i will be 0, so don't change values, keep all 'c'
        if i == 0:
            continue
        else:
            # copy the previous row to the extra list
            listTwo = copy.deepcopy(matrix[i - 1])

            # change the data just copied from matrix to extra list and change all values to lower
            listTwo = [item.lower() for item in listTwo]

            # skipCounter increments by i + 1 to skip by 2's, 3's, 4's etc based on the row
            skipCounter = i + 1

            # for loop that starts from 0 to number of columns, and skips every time by i + 1
            for b in range(i, inputCols, skipCounter):
                # if the value of the previous row is closed, change it to open, else change it to Closed
                if matrix[i - 1][b] == 'c':
                    listTwo[b] = "O"
                else:
                    listTwo[b] = 'C'
            # copy back the information saved in listTwo to the final matrix
            matrix[i] = copy.deepcopy(listTwo)

    # pprint method that prints a 2 dimensional matrix vertically rather than horizontally
    pprint.pprint(matrix)



postman()
