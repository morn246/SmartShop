import pymongo
import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import ShopClass 
from ConnectionToMongoDB import ConnectionDB
from pymongo import MongoClient
from sys import exit
import datetime



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
            if(2== chose):
                Con.addItemList()
            if(3== chose):
                Con.upItemList()
            if(4== chose):
                Con.delItemList()
            if(5== chose):
                s=ShopClass.ShoppList(Con)               
                Con.createList(s)
            if(6== chose):
                exit(0)
        except Exception as e:
            print("An exception occurred ",e) 
        
Con=ConnectionDB()

menu()






