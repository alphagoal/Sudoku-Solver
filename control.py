from solver_ver1 import countdown, load_file

def start():
    print("\nWelcome to Start Page .......")
    sel_format = input("Please enter your preferred sudoku input txt file format:\
        \n1. Comma Format --- Enter [1]\
        \n2. Other format (under development) --- Enter [2]\
        \nEnter [99] to exit the application.\n")
    print("")
    try:
        sel_format=int(sel_format)
    except ValueError:
        print("Sorry, you have entered the wrong input. Please try again.")
        start()

    if sel_format ==1:
        print("Txt File Format: 1. Comma. ")
        board = load_file()
        return board

    elif sel_format==2:
        print("Txt File Format: 2. Others ")
        print("Sorry, this format is still under development. Please select another choice.\n\n")
        result = start()
        return result

    elif sel_format ==99:
        print("\n\nThank you for using Sudoku application.\n~~ Bye Bye ~~\n\n\n")
        countdown(5)
        return "end"
    else:
        print("Sorry, you have entered the wrong input. Please try again.")
        start()