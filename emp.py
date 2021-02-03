from pymongo import MongoClient # import mongo client to connect
import pprint
# Creating instance of mongoclient
client = MongoClient()
# Creating database
db = Client.klu
employee = {
    "regno": "1099",
    "name":" CHNADU",
    "dept": "CSE",
    "salary" : "24000",
}
# Creating document
employees = db.employees
# Inserting data
employee.insert_one(employee)
# Fetching data
pprint.pprint(employee.find_one())

