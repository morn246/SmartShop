# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:03:57 2022

@author: 97252
"""
import pymongo
import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import ShopClass
from pymongo import MongoClient
from sys import exit
import datetime 

def xmlPross():
        tree = et.parse("AllPrice.xml")
        root=tree.getroot()
        b=0;
        ItemName=[]
        ItemPrice=[]
        Dict={}
        for time in root.iter('ItemName'):
            ItemName.append(time.text)
        for time in root.iter('UnitOfMeasurePrice'):
            ItemPrice.append(time.text)   
        for i in range(len(ItemName)):
            wordSp= ItemName[i].split()
            if(len(wordSp)>=1):        
                w=wordSp[0]
            #if(len(wordSp)>1):
                #w=wordSp[0]+" "+wordSp[1]          
            Dict[w]=[ItemPrice[i],ItemName[i]]
        return Dict

        
class ConnectionDB:
    
    def __init__(self):       
        self.Dict=xmlPross()       
        try:
            conn =pymongo.MongoClient("mongodb+srv://mor:123@cluster0.rmuim.mongodb.net/ShopTop?retryWrites=true&w=majority")
            conn.server_info()            
            db= conn["SmartShop"]
            self.collectionUser= db["Users"]
            self.user=self.login()
            self.collectionShopList= db["ShopList"]
            self.collectionShopListItem= db["ShopListItem"]
            
        except Exception as e:
            print("Error connection \n ", e)
            exit(0)
            
    def verify(self,user):    
            res=self.collectionUser.find_one({"name":user.name})
           
            if(res):
                if(res["passw"]==user.passw):
                    return True
            return False
    def login(self):
        i=0;        
        while(i<3):
            user=ShopClass.User()
            i=i+1
            if(self.verify(user)):
                return user
            else:
                print("Incorrect password or user Try again ")
        raise "The 3 attempts to connect fail out of the system"
        

    def createList(self,s):
        #s=ShopClass.ShoppList(self.ConnectionDB)
        shopListItem={"id":s.id,"shoppingDate":s.shoppingDate,"sumPrice":s.sumPrice,"actualPrice":s.actualPrice}       
        self.collectionShopList.insert_one(shopListItem)
        print("Budget updated successfully","The price according to the list ",int(s.sumPrice),"The actual price",s.actualPrice,)
        

    def calPrice(self,NameP):
        if(NameP in self.Dict):
           
            return self.Dict[NameP][0]
        return 0
    def getDet(self,NameP):
        if(NameP in self.Dict):            
            return self.Dict[NameP][1]
        return ""
    def find(self):
        p=self.collectionShopListItem.find({},{"name":""}) 

    def printList(self):  
        i=0
        results= self.collectionShopListItem.find({"isDone":False})  
        for r in results:
            i+=1
            print(" ",r["name"]," ",r["price"])#),r["date"])  
        print("The number of items in the list  ",": ",i)
    def addItemList(self):
        s= ShopClass.ShopListItem(self.user)
        shopItem={"id":s.id,"date":s.date,"name":s.name,"price":self.calPrice(s.name),"quantity":s.quantity,"user":(s.user).name,"Det":self.getDet(s.name),"ShoppingDate":s.shoppingDate,"isDone":s.isDone}       
        self.collectionShopListItem.insert_one(shopItem)
    
    def delItemList(self):
        name = input("Enter name for delete:")
        self.collectionShopListItem.delete_one({"name" : name})

    def upItemList(self,ID,name,change):
        filter = { "name": ID }
        newvalues = { "$set": { name: change } }
        self.collectionShopListItem.update_one(filter, newvalues)
        #self.collectionShopListItem.update_one({"name":ID},{"$set": {str(name):change}})

    def delAllItemList(self):        
        self.collectionShopListItem.delete_many({})

   