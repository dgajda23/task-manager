from Functions import *
from Task import *

# Method that displays the page for editing a task
def displayEditPage(service):
    # Getting the list of tasks by the provided month
    month = getMonth()
    listTasks = list(service.searchByMonth(month))
    printTasksByMonth(month, listTasks)
    oldTask = getTaskInfoNoMonth(month)
    taskToEdit = Task("", date(1, 1, 1), 1)
    copyTask(taskToEdit, oldTask)
    
    # Loop that asks the user what they want to change
    options = ["Change name", "Change date", "Change priority"]
    title = "What would you like to do?"
    selection = displayMenu(options, title)
    goBack = False
    if (selection == "Change name"):
        taskName = getName()
        taskToEdit.updateName(taskName)

    elif (selection == "Change date"):
        newDate = getDate()
        taskToEdit.updateDate(newDate)

    elif (selection == "Change priority"):
        prio2 = getPrio()
        taskToEdit.updatePrio(prio2)
    
    elif (selection == "Don't edit"):
        goBack = True

    # Return if the user wants to go back
    if (goBack == True):
        return
    
    editAddLoop(service, "Edit", taskToEdit, oldTask)