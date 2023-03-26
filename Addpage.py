# Page to add tasks
from Task import *
from simple_term_menu import TerminalMenu
from Functions import *

# Method that displays the page for adding a task
def displayAddPage(service):
    newTask = getAllTaskInfo()
    editAddLoop(service, "Add", newTask, None)