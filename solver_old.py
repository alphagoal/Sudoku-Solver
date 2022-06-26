from asyncio.windows_events import NULL
import time

def print_board(list1):
    #print("\nsudoku challenge - original board:".upper(),"\n")
    count = 0
    count_line=0
    for line in list1:
        for num in line:
            if count==0 or count%3!=0:
                print(num,end=" ")
                count+=1    #next time can use range and length
            else:
                print("|",end=" ")
                print(num, end=" ")
                count+=1    #next time can use range and length
        count =0
        count_line+=1       #next time can use range and length
        print(" ")
        if count_line==3 or count_line==6:
            for a in range(11):
                print("—",end="")
            print("")
    return None


def confirm_change(list1): #this can be simplified, if in ops we use num==0 to replace for checking
    changed_line=[]
    result=[]
    for line in list1:
        for num in line:
            if num>0:
                changed_line.append(1)
            else:
                changed_line.append(0)
        result.append(changed_line)
        changed_line=[]
    return result


def sqaure_list(list1):    
    #Can use another more efficient way next time!
    col_start=0 
    row_start=0
    sq_completed=0
    sq=[]
    new_list=[]
    "Or Express in the following way"
    #col_start, row_start, sq_completed,sq, new_list=(0,0,0,[],[])

    while sq_completed<9:
        if sq_completed!=0 and sq_completed%3==0:
            row_start+=3
            col_start=0
        elif sq_completed!=0:
            col_start+=3
        for x in range(row_start,row_start+3):
            sq.extend(list1[x][col_start:col_start+3])
        sq_completed+=1
        new_list.append(sq)
        sq=[]
    #Why is it different when using sq=[] vs sq.clear()
    return new_list

def column_list(list1):
    line_list=[]
    result=[]
    for x in range(9):
        for y in range(9):
            line_list.append(list1[y][x])
        result.append(line_list)
        line_list=[]
    return result


def ops(num, bo_confi, bo_row, bo_col, bo_sq):
    if bo_confi==0:
        while num<9:
            num+=1
            if num not in bo_row and num not in bo_col and num not in bo_sq:
                return num
        num = 0   
    return num



def sol_bo (prob):
    bo_confi=confirm_change(prob)
    bo_row=prob
    bo_col=column_list(prob)
    bo_sq=sqaure_list(prob)
    bo_sol=prob
    row, col =0,0

    while row<9: #can add: and row>=0
        # check row<0
        if row<0:
            print("\nYou are wrong! Game over!")
            return None

    #Error 1: Should put bo_sol instead of original prob board for the first variable in ops func
    #Error 2: Forget to reset the cell number to zero before backtracking
    #Error 3: Forget that bol_row, bo_col, bo_sq are dynamic and needs to update everytime! when num==0 and num!=0
        while col<9:
            sq_pos=int(row/3)*3+int(col/3)
            num=ops(bo_sol[row][col],bo_confi[row][col],bo_sol[row],bo_col[col],bo_sq[sq_pos])
            if num!=0:
                bo_sol[row][col]=num
                bo_col[col][row]=num
                bo_sq[sq_pos][row%3*3+col%3]=num
                print(f"Cell {row},{col} is:",num)
                col +=1
            else:
                
                print("\nBackward start position:",row,",",col)
                while num==0:
                    bo_sol[row][col]=num
                    col-=1
                    if col<0:
                        print("------------------------------  Checking the row before going back --------------- ---------------")
                        print(f"Row {row} is:",bo_sol[row])
                        row-=1
                        col=8
                    # check row<0
                    if row<0:
                        print("\nYou are wrong! Game over!")
                        return None
                    

                    print("Backward - Traceback:",row,",",col)
                    while bo_confi[row][col]!=0:
                        col-=1
                        if col<0:
                            row-=1
                            col=8
                        print("Backward - Find Empty Cell:",row,",",col)
                        # check row<0
                        if row<0:
                            print("\nYou are wrong! Game over!")
                            return None

                    print("Start analysis:",row,",",col)
                    sq_pos=int(row/3)*3+int(col/3)
                    print("Square position:",sq_pos)
                    print("Confirm Zero (needs to edit):",bo_confi[row][col])

                    num=ops(bo_sol[row][col],bo_confi[row][col],bo_sol[row],bo_col[col],bo_sq[sq_pos])
                    print("The new number is:",num)
                    print(f"Cell {row},{col} is:",num)
                    bo_sol[row][col]=num
                    bo_col[col][row]=num
                    bo_sq[sq_pos][row%3*3+col%3]=num
                    
                
                print("***** Finish cell:",row,",",col, f". Input num: {num} *****")
                
                
                print(f"***** Square is: {sq_pos}; Inside is:",row%3*3+col%3,"*****")
                print(f"Row {row} is:",bo_sol[row])
                col +=1
                print("Next item:",row,",",col)

        print(f"Row {row} is:",bo_sol[row])
        col=0
        row+=1
        
        print("Next row item:",row,",",col)

    print("\nFinish the whole board ......\n")
    for x in range(len(bo_sol)):
        print(f"Row {x} is:",bo_sol[x])

    return bo_sol


def countdown(time_sec):
    while time_sec:
        #mins, secs = divmod(time_sec, 60) #<--- gives a tuple: 1st is result, 2nd is remainder
        #timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #print(timeformat, end='\r')
        print('Screen will close in',time_sec, 'seconds......', end='\r')
        #\n : next line  ;  \r : same line appear replace old value
        time.sleep(1)
        time_sec -= 1

    #print("stop")
#countdown(5)

def txt_choice():
    txt_type = input("Please choose your txt file type: \n \
1. Comma ',' Format \n \
2. Dot '.' Format \n")
    print(f"Your input is: {txt_type} ... The input type is {type(txt_type)}...")
    print("Check if the input is correct: ", txt_type =="1" or txt_type =="2")

    if txt_type != "1" and txt_type !="2":
        print("Wrong Input. Please input again...\n")
        txt_choice()
    
    print("Checking ... func txt_choice() comes to the end ...")
    return txt_type

#txt_choice()

def load_txt():


#STEP 1: INPUT FILE AND LOAD THE FILE
    preference = NULL
    check_rerun = False

    while preference != "1" and preference !="2":
        preference = input("Choose your preferred setting:\n \
1. Run Default txt file\n \
2. Run your preferred txt file (in same directory)\n")
        
        #print(type(preference))
        #print("Your preference is:",preference)

        txt_type = NULL

        if preference =="1":
            txt_path = "case_1.txt"
            txt_type="1"

        elif preference =="2":
            txt_type = txt_choice()
                           
            txt_path = input("Choose your preferred txt file (in same directory):")

        else:
            print("Wrong Input. Reloading Request...")

    
    #txt_path = input("Please input the file path: ")
    #f=open(r'D:\User\Desktop\Python\proj_start\sudoku\sudoku\case_1.txt') 
    #because in ptrhon this char "\" may clash with other command, we need to slightly change the syntax  or use \\ or / in the directory
     

    try:
        f=open(txt_path,"r")
        print(f"The read file content is: {f}")
    except FileNotFoundError:
        print(f"Sorry, the file '{txt_path}' does not exist in current directory.\n\n Reloading Request...\n")
        #f.close
        load_txt()


#STEP 2: CHECK BOARD LENGTH

    board =list(f)
    print(f"The current board content is: {board} \n")

    if len(board)!=9:
        print("File is not in correct format. Total number of lines is not 9. \nRestarting Request ...")
        f.close
        load_txt()


#STEP 3A: Run Comma Type Txt File
    if txt_type=="1":
        for x in range(9):
            if x==8:
                if len(board[x])!=17:
                    print("File is not in correct format. The last line does not has 17 string. \nRestarting Request ...")
                    f.close
                    check_rerun = True
                    break #Evereything after break in same indent will be ignored
                    #load_txt()  # <--- Incorrect to do recursion inside the loop. Cuz after the recursion, it will continue to do looping using the older file.
            else:
                if len(board[x])!=18:
                    print(f"File is not in correct format. Line {x+1} does not has 18 string. \nRestarting Request ...")
                    f.close
                    check_rerun = True
                    break #Evereythin after break in same indent will be ignored
                    #load_txt()  # <--- Incorrect to do recursion inside the loop. Cuz after the recursion, it will continue to do looping using the older file.
 
        

        print(f"After checking, the current board content is: {board} \n")
        if check_rerun ==False:
            new_board=[]
    
            for k in range (len(board)):
                #n=0
                new_line=[]
                #for x in board[k]:
                new_line = board[k].split(",")
                for y in range(len(new_line)):
                    new_line[y]=int(new_line[y])
                new_board.append(new_line)

            #because it uses 2 for loops, the performance will be slower

# The recursion should be placed in the end, if in the middle of the loop, it will continue using the old rather than new one to run the codes after the command.
# Also, in next exercise, it is better to check all validity first before running the codes. This algorithm design will be better

        if check_rerun == True:
            new_board = load_txt()

        print(f"Type 1 txt board finish loading. The board is: {new_board} \n")
    
#STEP 3B: Run Dot Type Txt File
    if txt_type =="2":
        for x in range(9):
            if x==8:
                if len(board[x])!=9:  #the last value is eithere "\n" or "''"
                    print(f"Length of line {x} is: {len(board[x])} ")
                    print(list(board[x]))
                    print(f"File is not in correct format. Line {x+1} does not have 10 string. \nRestarting Request ...")
                    f.close
                    check_rerun = True # This is a gate checker before running the codes
                    break
                    #load_txt()  # <--- Incorrect to do recursion inside the loop. Cuz after the recursion, it will continue to do looping using the older file.
                    
            else:
                 if len(board[x])!=10:  #the last value is eithere "\n" or "''"
                    print(f"Length of line {x} is: {len(board[x])} ")
                    print(list(board[x]))
                    print(f"File is not in correct format. Line {x+1} does not have 10 string. \nRestarting Request ...")
                    f.close
                    check_rerun = True
                    break # This is a gate checker before running the codes
                    #load_txt() # <--- Incorrect to do recursion inside the loop. Cuz after the recursion, it will continue to do looping using the older file.
                   
 
                
        if check_rerun == False:
            new_board=[]
            for k in range(len(board)):
                #n=0
                new_line=[]
                for x in board[k]:
                    num_list='123456789'
                    if x in num_list:
                        new_line.append(int(x))
                    elif x==".":
                        new_line.append(0)
                    elif x=="\n":
                        pass
                    else:
                        print(f"File is not in correct format. The file has   other string. The string is: {x} \nRestarting Request ...")
                        f.close
                        check_rerun = True
                        break  # As alwways, This is a gate checker #check if it will still append new_board
                        
                if check_rerun == False:
                    new_board.append(new_line)
                else:
                    break

        
# The recursion should be placed in the end, if in the middle of the loop, it will continue using the old rather than new one to run the codes after the command.
# Also, in next exercise, it is better to check all validity first before running the codes. This algorithm design will be better

        if check_rerun == True:
            new_board = load_txt()

        print(f"Type 2 txt board finish loading. The board is: {new_board} \n")
        


    f.close

    return new_board

#load_txt()


"""
This is a comment
written in
more than just one line
"""


"""    
                if n%2==0:
                    new_line.append(int(x))
                n+=1
            new_board.append(new_line)
"""