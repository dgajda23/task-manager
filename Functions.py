from simple_term_menu import TerminalMenu
from Task import *
import config

# Method that asks the user for the name of a task
def getName():
    taskName = input("Type the name of the task and hit enter: ")
    return taskName

# Method that asks the user for the year of the task
def getYear():
    year = int(input("Enter what year this task is for (ex. 2023): "))
    return year

#Method that asks the user for the month of the task
def getMonth():
    options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    title = "Select a month and hit enter."
    monthString = displayMenu(options, title)
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

# Method that asks the user for the day of the task
def getDay():
    day = int(input("Enter what day the task is for: "))
    return day

# Method that asks the user for the priority of the task
def getPrio():
    prio = int(input("Enter the priority of the task (1-LOW priority, 5-HIGH priority): "))
    return prio

# Method that gets the whole date of a task from the user
def getDate():
    month = getMonth()
    day = getDay()
    year = getYear()
    newDate = date(year, month, day)
    return newDate

# Method that displays a menu for confirmation ("Yes", "No")
def confirmation(title):
    options = ["Yes", "No"]
    return displayMenu(options, title)

# Method that displays a selection menu that can be used with arrow keys
# Takes the options for the menu and the title
def displayMenu(options, titleMenu):
    terminal_menu = TerminalMenu(options, title=titleMenu)
    menu_entry_index = terminal_menu.show()
    print()
    return options[menu_entry_index]

# Method that prints the tasks of a given month
# Takes the month desired and list of tasks
def printTasksByMonth(month, list):
    print("Here are the tasks from " + config.months[month] + ":")
    for object in list:
        print(object['name'] + " - " + str(config.months[object['month']]) + " " + str(object['day']) + ", " + 
            str(object['year']) + " - Priority: " + str(object['prio']))
        print()

# Method that prints all tasks while also checking if they are late
# Takes a list of tasks
def printAllTasksWithLate(list):
    print("Here are your tasks:")
    print()
    for object in list:
        if (date.today() > date(object['year'], object['month'], object['day'])):
            print("LATE")
        print(config.months[object['month']] + " " + str(object['day']) + ", " + str(object['year']))
        print(object['name'])
        print("Priority: " + str(object['prio']))
        print()

# Method that gets task info from the user without asking for month
# Returns a new task object
def getTaskInfoNoMonth(month):
    name = getName()
    day = getDay()
    year = getYear()
    prio = getPrio()
    dateTask = date(year, month, day)
    task = Task(name, dateTask, prio)
    return task

# Method that gets all task info from the user
# Returns a new task object
def getAllTaskInfo():
    name = getName()
    year = getYear()
    month = getMonth()
    day = getDay()
    prio = getPrio()
    newDate = date(year, month, day)
    task = Task(name, newDate, prio)
    return task

# Method that deep copies one task to another
def copyTask(task1, task2):
    task1.updateName(task2.returnName())
    task1.updateDate(task2.returnDate())
    task1.updatePrio(task2.returnPrio())

# Method that returns a dictionary of the values of a task
def getDictTask(task):
    return({"name": task.returnName(), "month": task.returnDate().month,
                               "day": task.returnDate().day, "year": task.returnDate().year,
                                 "prio": task.returnPrio()})


# Method that executes a function from the service provided
# Takes the service, option, task, and old/new values for editing
def execService(service, option, task, old_values, new_values):
    if (option == "Add"):
        service.addTask(task.returnName(), task.returnDate().year, 
                        task.returnDate().month, task.returnDate().day, task.returnPrio())
    elif (option == "Edit"):
        service.editTask(old_values, new_values)

# Method that selects what is to be changed
# Takes a task and an options value from terminal menu
def changeSelector(task, selection):
    if (selection == "Change name"):
        taskName = getName()
        task.updateName(taskName)

    elif (selection == "Change date"):
        newDate = getDate()
        task.updateDate(newDate)

    elif (selection == "Change priority"):
        prio = getPrio()
        task.updatePrio(prio)

    else:
        print("Quitting.")
        return True
    return False

# Method that loops for the edit or add functionality of the program
# Takes in the service, option, and two tasks
def editAddLoop(service, option, task1, task2):
    old_values = {}
    new_values = {}
    done = False
    while (done == False):
        task1.printTaskInfo()
        message = "Is this information correct?"
        if (confirmation(message) == "Yes"):
            if(option == "Edit"):
                old_values = getDictTask(task2)
                new_values.update({"$set":getDictTask(task1)})

            execService(service, option, task1, old_values, new_values)
            done = True

            if (option == "Add"):
                print("Task added.")
            elif (option == "Edit"):
                print("Task changed.")
            input ("Press enter to continue...")

        else:
            if (option == "Edit"):
                copyTask(task1, task2)

            options = ["Change name", "Change date", "Change priority", "Return"]
            title = "What would you like to do?"
            selection = displayMenu(options, title)
            done = changeSelector(task1, selection)

# Method that displays options for the view pages
# Takes in a service, option, and month
def viewLoop(service, option, month):
    from Deletepage import displayDeletePage
    from Editpage import displayEditPage

    done = False
    print("What would you like to do?")
    options = ["Return to homepage", "Edit a task", "Delete a task", "Delete all tasks"]
    title = "Select an option below and hit enter"
    selection = displayMenu(options, title)

    while (selection != "Return to homepage" and done == False):
        if (selection == "Delete a task"):
            displayDeletePage(service)
            done = True
        elif (selection == "Edit a task"):
            displayEditPage(service)
            done = True
        elif (selection == "Delete all tasks"):
            message = "Are you sure you want to delete all tasks"
            if (confirmation(message) == "Yes"):
                if (option == "Month"):
                    service.deleteAllByMonth(month)
                    input("Deleted all tasks from " + str(config.months[month]) + ". Press enter to continue...")
                else:
                    service.deleteAll()
                    input("Deleted all tasks. Press enter to continue...")
                done = True    
        if done == False:     
            selection = displayMenu(options, title)
