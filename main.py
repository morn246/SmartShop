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
        print("1 הצג את הרשימה קניות הנוכחית", 
        "\n" , "2  תוסיף עוד פריט לרשימה",        
        "\n"  , "3 תעדכן מחיר פריט ברשימה",        
        "\n"      , "4 תמחק ", 
        "\n"      , "5 ,רשימת קניות נוצרה ",        
        "\n" ,  "6 עדכן רשימת תקציב","\n") 
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






