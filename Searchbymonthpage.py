# Page to search by date
from Addpage import *
from Deletepage import *
from Editpage import *
from Functions import *

# Method that displays the page to search tasks by month
def displaySearchByMonthPage(service):
    month = getMonth()
    listTasks = list(service.searchByMonth(month))
    printTasksByMonth(month, listTasks)
    input("Press enter to continue...")
    viewLoop(service, "Month", month)

    
