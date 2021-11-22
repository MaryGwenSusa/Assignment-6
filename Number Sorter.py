print("\33[95m Number Sorter \33[00m")
highest = secondHighest = secondLowest = lowest = 0 # first initialization (for creating variables with changing values)
rep = 1 # second initialization
"""These are variables created for changeable value
"""
while rep <= 4: # condition for one input line taken but can have specific repetition
    try: # input validation
        inputNumber = float(input("Enter number " + str(rep) + ": "))
    except ValueError as alpha:
        print(f"\033[41m WARNING: \033[00m \033[96m You did not type in number format.\033[00m \033[31m{alpha}\033[00m")
        continue # loop
    """This will display a statement when the user did not put proper values and will loop the input function number
    """
    if inputNumber <= -1: # consider first initialization is zero
        print("\033[42m I'm sorry, I don't understand numbers below 1.\033[00m \033[93m Please input other numbers.\033[00m")
        continue # loop again
    else: # since there is an initial value, utilization of if-elif structure on reassignments of variables from lowest to highest and finally assigning the input (each condition, each variable level).
        if inputNumber > highest:
            lowest = secondLowest
            secondLowest = secondHighest
            secondHighest = highest
            highest = inputNumber
        elif  inputNumber > secondHighest:
            lowest = secondLowest
            secondLowest = secondHighest
            secondHighest = inputNumber
        elif inputNumber > secondLowest:
            lowest = secondLowest
            secondLowest = inputNumber
    rep += 1 # increment for number sequence of input function repetition
    

