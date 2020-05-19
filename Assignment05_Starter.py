# ---------------------------------------------------------------- #
# Title: Assignment05
# Description: Working with Dictionaries and Files
#                When the program starts, load each "row" of data
#                in "ToDoList.txt" into a python Dictionary.
#                Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CMcNiff,5.16.2020,Modified script
# CMcniff, 5.17,2020, Modified script to complete assignment
# ---------------------------------------------------------------- #
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries row (like Lab 5-2)
NewFile = open(objFile, "r")
for row in NewFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0] , "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
NewFile.close()

# Step 2 - Display a menu of choices to the user
while (True):
    print("""""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which 0ption would you like to perform? [1 to 5] - "))
    print() # adding a new line for looks

    # Step 3 - Show current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["Task"] + "," + dicRow["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a task: ")
        strPriority = input("Enter a priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while(True):
            taskRemoved = (input("Remove which task: "))
            for dicRow in lstTable:
                if dicRow["Task"] == taskRemoved:
                    lstTable.remove(dicRow)
                    print("Task Removed")
                    break
            else:
                print("Task not found")
            break


    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        Newfile = open(objFile, 'w')
        for dicRow in lstTable:
            Newfile.write(dicRow["Task"] + ',' + dicRow["Priority"] + "\n")
        print("Thank you for your input")
        Newfile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
      break # and Exit the program







