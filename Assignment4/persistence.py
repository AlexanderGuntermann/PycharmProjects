def persistence_to_one_digit(number):
    # set number to 1
    finalAnswer = 1
    count = 0

    # for every digit in a number, multiply each one by itself and set that to finalAnswer
    for num in number:
            finalAnswer *= int(num)
    # print out the digits multiplied by one another
    print("Prior Step: ",finalAnswer)
    # if the number is larger than two digits, call recursively with that number until its less than 10
    if finalAnswer >= 10:
        return persistence_to_one_digit(str(finalAnswer))

    return finalAnswer

# here are the example cases from the assignment
print("Number = 39")
example = persistence_to_one_digit("39")
print("Persistence of 39: ",example,"\n")

print("Number = 999")

exampleTwo = persistence_to_one_digit("999")
print("Persistence of 999: ",exampleTwo,"\n")

print("Number = 4")

exampleThree = persistence_to_one_digit("4")
print("Persistence of 4: ",exampleThree,"\n")

