# Main program file
from Homepage import *
from Addpage import *
from Listpage import *
from Searchbymonthpage import *
import rpyc

# Connecting to the microservice
conn = rpyc.connect("localhost", 18861)
service = conn.root

selection = displayHomeMenu()

# Application loop
while (selection != "Quit"):
    if (selection == "Add a task"):
        # Add task page
        displayAddPage(service)

    elif (selection == "View list of tasks"):
        # View the list page
        displayListPage(service)

    elif (selection == "Search tasks by month"):
        # Search by date page
        displaySearchByMonthPage(service)

    selection = displayHomeMenu()

# Quitting
print("Till next time!!")
conn.close()

