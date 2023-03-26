# Microservice that connects to a mongodb database and performs various CRUD operations
import rpyc 
import pymongo

from pymongo import MongoClient

class dbService(rpyc.Service):

    def on_connect(self, conn):
        # Method when clients connects to the server
        print("Client connected")
        # Connecting to the mongodb
        try:
            global client
            conn_str = "mongodb://dgajda:dgajda@ac-e1508em-shard-00-00.zxjtz0j.mongodb.net:27017,ac-e1508em-shard-00-01.zxjtz0j.mongodb.net:27017,ac-e1508em-shard-00-02.zxjtz0j.mongodb.net:27017/?ssl=true&replicaSet=atlas-62nydq-shard-0&authSource=admin&retryWrites=true&w=majority"
            client = MongoClient(conn_str)
            print("Successfully connected to database.")
        except Exception:
            print("Error:" + Exception)

    def on_disconnect(self, conn):
        # Method when client disconnects
        print("Client disconnected")

    # Method that adds a task given the values to add
    def exposed_addTask(self, nameToAdd, yearToAdd, monthToAdd, dayToAdd, prioToAdd):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        # Create a JSON object of task
        newTask = {"name": nameToAdd,
                   "year": yearToAdd,
                   "month": monthToAdd,
                   "day": dayToAdd,
                   "prio": prioToAdd}

        id = myCollection.insert_one(newTask)

        print("Task added.")
        return id

    # Method that returns all tasks sorted in the database
    def exposed_getAllTasks(self):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        listOfTasks = myCollection.find()
        
        sortedList = sorted(listOfTasks, key=lambda x: (x["year"], x["month"], x["day"], x["prio"], x["name"]))

        print("Tasks returned.")

        return sortedList
    
    # Method that returns a task by its date
    def exposed_searchByDate(self, monthToSearch, dayToSearch, yearToSearch):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        tasksByDate = myCollection.find({"month": monthToSearch, "day": dayToSearch, "year": yearToSearch})

        sortedList = sorted(tasksByDate, key=lambda x: (x["year"], x["month"], x["day"], x["prio"], x["name"]))
        
        print("Tasks returned.")

        return sortedList
    
    # Method that returns a sorted list of tasks for the given month
    def exposed_searchByMonth(self, monthToSearch):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        tasksByMonth = myCollection.find({"month": monthToSearch})

        sortedList = sorted(tasksByMonth, key=lambda x: (x["year"], x["month"], x["day"], x["prio"], x["name"]))

        return sortedList
    
    # Method that deletes a task given all its properties (name, day, month, year, and prio)
    def exposed_deleteTask(self, nameToDelete, monthToDelete, dayToDelete, yearToDelete, prioToDelete):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        myCollection.delete_one({"name": nameToDelete, "month": monthToDelete, "day": dayToDelete, "year": yearToDelete, "prio": prioToDelete})

    # Method that deltes all tasks in the database
    def exposed_deleteAll(self):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        myCollection.delete_many({})

    # Method that edits the task specified by "query" to the values given in "new_values"
    def exposed_editTask(self, query, new_values):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        myCollection.update_one(query, new_values)

    # Method that deletes all tasks given a month
    def exposed_deleteAllByMonth(self, monthToDelete):
        myDb = client["taskDb"]
        myCollection = myDb["tasks"]

        myCollection.delete_many({"month": monthToDelete})

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(dbService, port=18861)
    server.start()
   
