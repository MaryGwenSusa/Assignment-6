print("\33[95m Number Sorter \33[00m")
highest = secondHighest = secondLowest = lowest = 0 # first initialization (for creating variables with changing values)
rep = 1 # second initialization
while rep <= 4: # condition for one input line taken but can have specific repetition
    try: # input validation
        inputNumber = float(input("Enter number " + str(rep) + ": "))
    except ValueError as alpha:
        print(f"\033[41m WARNING: \033[00m \033[96m You did not type in number format.\033[00m \033[31m{alpha}\033[00m")
        continue
    if inputNumber <= -1: # consider first initialization is zero
        print("\033[42m I'm sorry, I don't understand numbers below 1.\033[00m \033[93m Please input other numbers.\033[00m")
        continue
    rep += 1 # increment for starting number of repetition of input function
    

