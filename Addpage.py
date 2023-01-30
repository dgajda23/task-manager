# Page to add tasks
from Task import *
from simple_term_menu import TerminalMenu

def getName():
    taskName = input("Type the name of the task you would like to add and hit enter: ")
    return taskName

def getYear():
    year = int(input("Enter what year this task is for (ex. 2023): "))
    return year

def getMonth():
    monthToAdd = 0
    options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    terminal_menu = TerminalMenu(options, title="Select a month and hit enter.")
    menu_entry_index = terminal_menu.show()

    monthString = options[menu_entry_index]
    month = 0

    if (monthString == "January"):
        month = 1
    
    if (monthString == "February"):
        month = 2
    
    if (monthString == "March"):
        month = 3
      
    if (monthString == "April"):
        month = 4
    
    if (monthString == "May"):
        month = 5
    
    if (monthString == "June"):
        month = 6
    
    if (monthString == "July"):
        month = 7
    
    if (monthString == "August"):
        month = 8
    
    if (monthString == "September"):
        month = 9
    
    if (monthString == "October"):
        month = 10
    
    if (monthString == "November"):
        month = 11

    if (monthString == "January"):
        month = 12
    return month

def getDay():
    day = int(input("Enter what day the task is for: "))
    return day

def getPrio():
    prio = int(input("Enter the priority of the task (1-LOW priority, 5-HIGH priority): "))
    return prio

def confirmation():
    options = ["Yes", "No"]
    terminal_menu = TerminalMenu(options, title="Is this information correct?")
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]

def displayAddPage():
    print("This is the add page")

    taskName = getName()
    year = getYear()
    month = getMonth()
    day = getDay()
    prio = getPrio()

    newDate = date(year, month, day)
    newTask = Task(taskName, newDate, prio)

    done = False
    while (done == False):
        newTask.printTaskInfo()
        if (confirmation() == "Yes"):
            # Add to database
            done = True
            print ("Added to your tasks.")
        else:
            options = ["Change name", "Change date", "Change priority", "Don't add"]
            terminal_menu = TerminalMenu(options, title="What would you like to do?")
            menu_entry_index = terminal_menu.show()

            if (options[menu_entry_index] == "Change name"):
                taskName = getName()
                newTask.updateName(taskName)

            elif (options[menu_entry_index] == "Change date"):
                year = getYear()
                month = getMonth()
                day = getDay()
                newDate = date(year, month, day)
                newTask.updateDate(newDate)

            elif (options[menu_entry_index] == "Change priority"):
                prio = getPrio()
                newTask.updatePrio(prio)

            else:
                print("Quitting.")
                done = True


    



    

    