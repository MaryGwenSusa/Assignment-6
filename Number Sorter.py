print("\33[95mNumber Sorter\33[00m")
highest = secondHighest = secondLowest = lowest = 0 # first initialization (for creating variables with changing values)
rep = 1 # second initialization
"""These are variables created for changeable value
"""
while rep <= 4: # condition for one input line taken but can have specific repetition
    try: # input validation
        inputNumber = float(input("\033[93mENTER NUMBER" + str(rep) + ": "))
    except ValueError as alpha:
        print(f"\033[41mWARNING:\033[00m \033[96mYou did not type in number format.\033[00m \033[31m{alpha}\033[00m")
        continue # loop
    """This will display a statement when the user did not put proper values and will loop the input function number
    """
    if inputNumber <= -1: # consider first initialization is zero
        print("\033[42mI'm sorry, I don't understand numbers below 1.\033[00m \033[93mPlease input other numbers.\033[00m")
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
        elif inputNumber > lowest:
            lowest = inputNumber
    rep += 1 # increment for number sequence of input function repetition
else:
    print(f"\033[00m\033[92mThe order from\033[00m \033[94mHIGHEST\033[00m \033[92mto\033[00m \033[93mlowest\033[00m  \033[92mare \33[95m{highest: .2f},\33[00m \033[91m{secondHighest: .2f},\33[00m \33[93m{secondLowest: .2f},\33[00m \033[92mand\33[00m \033[91m{lowest: .2f}.\033[00m")