

import pymongo
from pymongo import MongoClient


myclient =pymongo.MongoClient("mongodb+srv://mor:123@cluster0.rmuim.mongodb.net/ShopTop?retryWrites=true&w=majority")

#myclient = pymongo.MongoClient('mongodb+srv://mor:123@cluster0.mongodb.net/ShopTop?retryWrites=true&w=majority')


mydb = myclient["mydatabase"]
print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

"""
cluster = pymongo.MongoClient("mongodb+srv://mor:123@cluster0.rmuim.mongodb.net/ShopTop?retryWrites=true&w=majority")
#db = client.test


#s="mongodb+srv://mor:mn246246@cluster0.rmuim.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#cluster = MongoClient(s)


db= cluster["ShopTop"]
collection= db["Shop"]


  
  
print(cluster," /n  " ,collection)
shopItem={"_name":1,"price":20,"det":"bla"}
collection.insert_one(shopItem)


# name = input("Enter name:")
# price = input("Enter price:")
# det = input("Enter det:")

#s1= shopItem()
#print(s1.name," ",s1.price)
"""

