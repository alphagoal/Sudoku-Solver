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

#record git hub

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


"""
list1= [8,7,5]
list2=list1
list3=list(list1)
list1.append("a")
print(list2)
print(list3)
"""

"""
This is a comment
written in
more than just one line
"""
