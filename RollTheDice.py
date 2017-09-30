#This is a "Roll the Dice Program"
#Declareed the value of leave_program.
leave_program = 0
#Overall "while loop" as long as the input from user is not 'q' than the program will continue.
while leave_program != "q":
    #Lines 7 and 8 will be displayed for the user to see when program is running for guidance.
    print("THIS IS A ROLL THE DICE PROGRAM")
    print("Press ENTER to roll the dice")
    #Line 10 takes input from user to execute program.
    input()
    #Line 11 tells Python that the "random" module will be used for this program.
    import random
    #Line 14 identified that Python will "randomly" pick a value between 1 and 6 to display to the user.
    number = random.randint(1,6)
    if number == 1:
        print("---------")
        print("---------")
        print("----o----")
        print("---------")
        print("---------")
        print("Type 'q' to quit program or 'ENTER' to play again.")
        leave_program = input()
    if number == 2:
        print("---------")
        print("---------")
        print("--o---o--")
        print("---------")
        print("---------")
        print("Type 'q' to quit program or 'ENTER' to play again.")
        leave_program = input()
    if number == 3:
        print("-------o-")
        print("---------")
        print("----o----")
        print("---------")
        print("-o-------")
        print("Type 'q' to quit program or 'ENTER' to play again.")
        leave_program = input()
    if number == 4:
        print("---------")
        print("-o-----o-")
        print("---------")
        print("-o-----o-")
        print("---------")
        print("Type 'q' to quit program or 'ENTER' to play again.")
        leave_program = input()
    if number == 5:
        print("---------")
        print("-o-----o-")
        print("----o----")
        print("-o-----o-")
        print("---------")
        print("Type 'q' to quit program or 'ENTER' to play again.")
        leave_program = input()
    if number == 6:
        print("---------")
        print("-o-----o-")
        print("-o-----o-")
        print("-o-----o-")
        print("---------")
        print("Type 'q' to quit program or 'ENTER' to play again.")
        leave_program = input()
else:
    print("Thank you for playing. AND REMEMBER GAMBLING CAN BE ADDICTIVE!")
