def print_board(list1):
    #print(type(list1),"\n")
    print("\nsudoku challenge - original board:".upper(),"\n")
    count = 0
    count_line=0
    for line in list1:
        for num in line:
            if count==0 or count%3!=0:
                print(num,end=" ")
                count+=1
            else:
                print("|",end=" ")
                print(num, end=" ")
                count+=1
        count =0
        count_line+=1
        print(" ")
        if count_line==3 or count_line==6:
            for a in range(22):
                print("—",end="")
            print("")
    return None

def confirm_change(list1):
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
    num_start=0
    line_start=0
    sq=[]
    sq_completed=0
    new_list=[]
    #sq0=list1[0][0:3]+list1[1][0:3]+list1[2][0:3]
    #sq1=list1[0][3:6]+list1[1][3:6]+list1[2][3:6]
    #sq3=list1[3][0:3]+list1[4][0:3]+list1[5][0:3]
    while sq_completed<9:
        if sq_completed!=0 and sq_completed%3==0:
            line_start+=3
            num_start=0
        elif sq_completed!=0:
            num_start+=3
        for x in range(line_start,line_start+3):
            sq.extend(list1[x][num_start:num_start+3])
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


prob=[[0,0,6,0,9,0,2,0,0],[0,0,0,7,0,2,0,0,0],[0,9,0,5,0,8,0,7,0],[9,0,0,0,3,0,0,0,6],[7,5,0,0,0,0,0,1,9],[1,0,0,0,4,0,0,0,5],[0,1,0,3,0,9,0,8,0],[0,0,0,2,0,1,0,0,0],[0,0,9,0,8,0,1,0,0]]

print_board(prob)
prob_sq=sqaure_list(prob)
prob_col=column_list(prob)

print("")
print("Confirming if the values need changes...\n(0=No; 1=Yes)\n")
confirm_list=confirm_change(prob)
count_line=0
for line in confirm_list:
    count_line+=1
    print(f"Confirm Row {count_line}:",line)

print("\n")
print("Analyzing squares...")
count_line=0
for line in prob_sq:
    count_line+=1
    print(f"Square {count_line} is:",line)

print("")
print("Analyzing columns...")
count_line=0
for line in prob_col:
    count_line+=1
    print(f"Column {count_line} is:",line)
