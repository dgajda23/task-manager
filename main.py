# Main program file

from Homepage import *
from Addpage import *
from Calendarpage import *
from Listpage import *
from Searchbydateage import *

selection = displayHomeMenu()

# Application loop
while (selection != "Quit"):
    if (selection == "Add a task"):
        # Add task page
        displayAddPage()
        print("ADD TAKSK")

    elif (selection == "View list of tasks"):
        # View the list page
        displayListPage()
        print("View list")

    elif (selection == "View calendar"):
        # View the calendar page
        displayCalendarPage()
        print("view")

    elif (selection == "Search tasks by date"):
        # Search by date page
        displaySearchByDatePage()
        print("search")

    elif (selection == "Quit"):
        # Quit program
        print("quit")

    selection = displayHomeMenu()