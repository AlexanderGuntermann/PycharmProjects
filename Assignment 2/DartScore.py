


def scoreThrows():



    numberOfThrows = input("Please input the number of throws you are scoring: ") # input number of throws to score

    if numberOfThrows == 0:
        print("You scored 0")

    myList = [] # array to store throws

    countBonus = 0 # keep track of all scores below 5.

    for i in range(numberOfThrows): # a loop for adding each score to the array
        myList.append(input("Please input your scores: "))
        if myList[i] < 5: # conditional statement to keep track of the number of scores below 5
            countBonus = countBonus +1


    scoreCount = 0

    for i in range(myList.__len__()): # loop to determine scoring for each throw
        if myList[i] > 10:
            scoreCount += 0
        if myList[i] >= 5 and myList[i] <= 10:
            scoreCount += 5
        if myList[i] < 5:
            scoreCount += 10

    if (countBonus == myList.__len__()) and numberOfThrows > 0: # conditional statement to determine if all scores are less that 5
        scoreCount += 100
        print("You earned 100 bonus points having all radius less than 5!")

    print ("Your total score was: " + str(scoreCount))


scoreThrows()
