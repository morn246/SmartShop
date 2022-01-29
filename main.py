import pymongo
import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import ShopClass 
from ConnectionToMongoDB import ConnectionDB
from pymongo import MongoClient
from sys import exit
import datetime
import numpy as np



def menu():    
    while True:        
        print("1- View the current shopping list", 
        "\n" , "2- Add another item to the list",        
        "\n"  , "3- Update the price of a particular item",        
        "\n"      , "4- Delete the item", 
        "\n"      , "5- Update the budget of the shopping list",        
        "\n" ,  "6- Exit","\n") 
        try:
            chose= int(input())  
            if(1== chose):
                Con.printList()
            elif(2== chose):
                Con.addItemList()
            elif(3== chose):
                Con.upItemList()
            elif(4== chose):
                Con.delItemList()
            elif(5== chose):
                s=ShopClass.ShoppList(Con)               
                Con.createList(s)
            elif(6== chose):
                exit(0)
        except Exception as e:
            print("An exception occurred ",e) 
            
            

 



Con=ConnectionDB()



Con.CalBudgetPerMonth(2021)
#s= ShopClass.ShopListItem(Con.user)
# shopItem={"id":s.id,"date":s.date,"name":"תה","price":Con.calPrice("תה"),"quantity":s.quantity,"user":(s.user).name,"Det":Con.getDet(s.name),"ShoppingDate":s.shoppingDate,"isDone":s.isDone}      
# Con.collectionShopListItem.insert_one(shopItem)
# s.nam="קורנפלור"
# shopItem={"id":s.id,"date":s.date,"name":"שניצל","price":Con.calPrice("שניצל"),"quantity":s.quantity,"user":(s.user).name,"Det":Con.getDet(s.name),"ShoppingDate":s.shoppingDate,"isDone":s.isDone}      
# Con.collectionShopListItem.insert_one(shopItem)
# s.nam="שקדים"
# shopItem={"id":s.id,"date":s.date,"name":"טחינה","price":Con.calPrice("טחינה"),"quantity":s.quantity,"user":(s.user).name,"Det":Con.getDet(s.name),"ShoppingDate":s.shoppingDate,"isDone":s.isDone}      
# Con.collectionShopListItem.insert_one(shopItem)
# s.nam="מוסקט"
# shopItem={"id":s.id,"date":s.date,"name":"סטייק","price":Con.calPrice("סטייק"),"quantity":s.quantity,"user":(s.user).name,"Det":Con.getDet(s.name),"ShoppingDate":s.shoppingDate,"isDone":s.isDone}      
# Con.collectionShopListItem.insert_one(shopItem)
# s=ShopClass.ShoppList(Con)               
# Con.createList(s)
#menu()






