import pymongo
import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import ShopClass 
from ConnectionToMongoDB import ConnectionDB
from pymongo import MongoClient
from sys import exit
import datetime


"""
def xmlPross():
    tree = et.parse("AllPrice.xml")
    root=tree.getroot()
    b=0;
    ItemName=[]
    ItemPrice=[]
    for time in root.iter('ItemName'):
        ItemName.append(time.text)
    for time in root.iter('UnitOfMeasurePrice'):
        ItemPrice.append(time.text)
    
    for i in range(len(ItemName)):
        wordSp= ItemName[i].split()
        if(len(wordSp)==1):        
            w=wordSp[0]
        if(len(wordSp)>1):
            w=wordSp[0]+" "+wordSp[1]
            
        Dict[w]=ItemPrice[i]
        
#Timestamp.append(time.text)
def calPrice(NameP):
    if(NameP in Dict):
        print("true",  Dict[NameP])
        return Dict[NameP]
    return 0
    
            
def addItemList():
    s= ShopListItem()
    shopItem={"name":s.name,"price":calPrice(s.name),"det":s.det}
    #s.price= calPrice(s.name)
    #4
    print(s.price)
    collection.insert_one(shopItem)
    
def delItemList():
    name = input("Enter name for delete:")
    collection.delete_one({"name" : name})

def upItemList():
    name = input("Enter name for update:")
    name1=input("Enter new price")
    resultUp= collection.update_one({"name":name},{"$set": {"price":name1}})

def delAllItemList():
    collection.delete_many({})
    
def printList():
    post_count = collection.count_documents({})  
    print("מספר הפרטים ברשימה ",": ",post_count)
    results= collection.find({})  
    for r in results:
        print(" ",r["name"]," ",r["price"])

#def createList():
 #     post_count = collection.count_documents({}) 
 #     ShoppList(collection ,post_count)
     
     
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher

# global collection
# try:
#     conn =pymongo.MongoClient("mongodb+srv://mor:123@cluster0.rmuim.mongodb.net/ShopTop?retryWrites=true&w=majority")
#     conn.server_info()
#     db= conn["ShopTop"]
#     collection= db["Shop"]
# except Exception as e:
#     print("Error connection \n ", e)
#     exit(0)
    

#Dict={}
#xmlPross()
"""

def menu():    
    while True:        
        print("1 הצג את הרשימה קניות הנוכחית", 
        "\n" , "2  תוסיף עוד פריט לרשימה",        
       "\n"  , "3 תעדכן מחיר פריט ברשימה",        
       "\n"      , "4 תמחק ", 
       "\n"      , "5 ,רשימת קניות נוצרה ",        
       "\n" ,  "6 תצא מהמערכת","\n") 
        try:
            chose= int(input())  
            if(1== chose):
                Con.printList()
            if(2== chose):
                Con.addItemList()
            if(3== chose):
                Con.upItemList()
            if(4== chose):
                Con.delItemList()
            if(5== chose):
                s=ShopClass.ShoppList(Con)
                print("succcccccccccc ")
                Con.CreateList(s)
            if(6== chose):
                exit(0)
        except Exception as e:
            print("An exception occurred ",e) 
        
Con=ConnectionDB()
menu()







