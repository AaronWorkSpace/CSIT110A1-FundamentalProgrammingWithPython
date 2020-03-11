#Done by: Aaron Lim
#Date: 05/10/2018
#Assignment 1

#Provided in assignment 1
import csv

#variable for the criteria (boolean)
#If ok is True, the loop will go on
#If ok is False, the loop will exit
ok = True
#variables
MOD110 = 'CSIT110'
MOD121 = 'CSIT121'
MOD135 = 'CSIT135'
MOD142 = 'CSIT142'
studentID = 'student_id'
fName = 'first_name'
lName = 'last_name'
printStudID = 'Student ID'
printFName = 'First Name'
printLName = 'Last Name'
printAvg = 'Average'
#Setting the criteria to exit the while loop
while(ok == True):
    #Getting user input
    studID = input("Enter student ID: ")
    #Setting all lower case characters to upper case characters
    studID = studID.upper()
    #Read and display the data.csv file (Provided in assignment 1)
    filePath = "data.csv"
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        #Checking if user entered an empty string
        if(studID == ""):
            print("Empty input, please enter again.")
        else:
            #Setting the variable for whether the student is inside
            #False for no student record found
            #True for student record found
            inside = False
            #Reading row by row
            for row in reader:
                #Checking if user input matches with any inside the list in excel (match any student id)
                if(studID == row["student_id"]):
                    #if match variable is set to true
                    inside = True
                    #Printing out the listing
                    print("=================")
                    print("Student's details")
                    print("=================")
                    print("{0:<11}|{1:^12}| {2}".format(printStudID, printFName, printLName))
                    print("{0:<11}|{1:>12}| {2:<1}".format(row[studentID], row[fName], row[lName]))
                    print("===============================================")
                    print("{0:<8}|{1:^9}|{2:^9}|{3:^9}|{4:^9} ".format(MOD110, MOD121, MOD135, MOD142, printAvg))
                    avg = (int(row[MOD110]) + int(row[MOD121]) + int(row[MOD135]) + int(row[MOD142]))/4
                    print("{0:^7} |{1:^9}|{2:^9}|{3:^9}|{4:^9} ".format(row[MOD110], row[MOD121], row[MOD135], row[MOD142], avg))
                    print("===============================================")
                    break
            #No student record found (False)
            if(inside == False):
                #Seperator and extra statement needed to be print out 
                print("========================")
                print("No student record found.")
                print("========================")
            #Variable to check if user want to continue
            #True for user entered an invalid character
            #False for continue / discontinue inputting value            
            okay = True
            while(okay == True):
                yesNo = input("Enter whether you want to continue entering another student ID (Y/N): ")
                yesNo = yesNo.upper()
                if(yesNo == "Y"):
                    ok = True
                    okay = False
                elif(yesNo == "N"):
                    ok = False
                    okay = False
                else:
                    print("You entered an invalid character(s), please enter again.")                
#Printing final message      
print("Thank you for using this program, see you again.")