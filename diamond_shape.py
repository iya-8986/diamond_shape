#author__thea_uy
#date__September_26_2024

#Write a Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.

#create a loop for the whole program
while True:
    try:
        number_of_rows = int(input("Enter the number of rows: ")) #get an input from user about the number of rows

        if number_of_rows%2 == 0: #if the user entered a even number, the user has to give another number that is odd. 
            print("Enter an odd number of rows: ")
            continue
        
        elif number_of_rows%2 != 0: #if the input is odd, the program will go to the next block of code. 
            pass

    except:
        continue
        
    rows = int((number_of_rows-1)/2) #get the row number for the small part of the diamond 

    for a in range(rows):
        for b in range(a,rows): #this line aims to create a decreasing invisible triangle
            print(" ", end=" ")

        for c in range(a): #this line will create a right side triangle
            print("*", end = " ")
        
        for d in range(1): #this line is intended for the middle section of the upper part of the diamond
            print("*", end = " ")
            
        for e in range(a): #this line will create an increasing right side triangle
            print("*", end = " ")
        print()

    for f in range(1): #this line is intended for the middle section of the entire diamond. 
        for g in range(number_of_rows):
            print("*", end= " ")
        print()

    for h in range(rows): 
        for i in range(h+1): #this line will create a invisible, increasing triangle
            print(" ", end = " ")
        
        for j in range(h, rows-1): #this line will create a decreasing right side triangle
            print("*", end = " ")
        
        for k in range(1): #this line is intended for the middle section of the lower part of the diamond. 
            print("*", end = " ")
        for l in range(h,rows-1): #this will create a decreasing triangle
            print("*", end = " ")
    
        print()

    #ask the use if they would want to try again
    while True:
        ans = str(input("Do you want to try again? Yes or No: "))
        upper_ans = ans.upper()
        if upper_ans == "YES":
            break
        elif upper_ans == "NO":
            print("\nThank you for using my program!")
            exit()
        else:
            print("Invalid Input")    


#end of the program



        

