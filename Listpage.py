# Page to view tasks in a list 
from Task import *
from Deletepage import *
from Editpage import *
from datetime import date
from Functions import *

# Method that displays the list page of the application
def displayListPage(service):
    # Getting the list of tasks
    listTasks = service.getAllTasks()
    theList = list(listTasks)
    
    # Printing out all the tasks also as well as a "LATE" message if it is late
    printAllTasksWithLate(theList)

    input("Press enter to continue...")
    viewLoop(service, None, None)