def is_triangle(stickA, stickB, stickC):

    if stickA > stickB + stickC or stickB > stickA + stickC or stickC > stickA + stickB:
        print("You can't make a triangle")
        return False
    else:
        print "You can make a triangle!"
        return True




def start_triangle_check():                        # prompt the user to input 3 stick length values which will be later
                                                   # used to determine if is_triangle will be true

    stickA = input("Please input the value for stickA: ")
    stickB = input("Please input the value for stickB: ")
    stickC = input("Please input the value for stickC: ")


    is_triangle(int(stickA),int(stickB),int(stickC)) #use function is_triangle with input casted to an int to determine if triangle


start_triangle_check()