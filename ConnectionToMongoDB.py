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
            self.user=self.Login()
            self.collectionShopList= db["ShopList"]
            self.collectionShopListItemt= db["ShopListItem"]
            
        except Exception as e:
            print("Error connection \n ", e)
            exit(0)
            
    def verify(self,user):    
            res=self.collectionUser.find_one({"name":user.name})
           
            if(res):
                if(res["passw"]==user.passw):
                    return True
            return False
    def Login(self):
        i=0;        
        while(i<3):
            user=ShopClass.User()
            i=i+1
            if(self.verify(user)):
                return user
            else:
                print("הסיסמא או המשתמש שגויים נסה שוב")
        raise "שלושת הנסיונות להתחבר שגויים יוצא מהמערכת"
        

    def CreateList(self,s):
        #s=ShopClass.ShoppList(self.ConnectionDB)
        shopListItem={"_id":s.id,"shoppingDate":s.shoppingDate,"sumPrice":s.sumPrice,"actualPrice":s.actualPrice}       
        self.collectionShopList.insert_one(shopListItem)
        print("finish")
        

    def calPrice(self,NameP):
        if(NameP in self.Dict):
           
            return self.Dict[NameP][0]
        return 0
    def getDet(self,NameP):
        if(NameP in self.Dict):            
            return self.Dict[NameP][1]
        return ""
    def find(self):
        p=self.collectionShopListItemt.find({},{"name":""}) 

    def printList(self):
        #post_count = self.collectionShopListItemt.count_documents({})  
        i=0
        results= self.collectionShopListItemt.find({"isDone":False})  
        for r in results:
            i+=1
            print(" ",r["name"]," ",r["price"])#),r["date"])  
        print("מספר הפרטים ברשימה ",": ",i)
    def addItemList(self):
        s= ShopClass.ShopListItem(self.user)
        shopItem={"id":s.id,"date":s.date,"name":s.name,"price":self.calPrice(s.name),"quantity":s.quantity,"user":(s.user).name,"Det":self.getDet(s.name),"ShoppingDate":s.shoppingDate,"isDone":s.isDone}       
        self.collectionShopListItemt.insert_one(shopItem)
    
    def delItemList(self):
        name = input("Enter name for delete:")
        self.collectionShopListItemt.delete_one({"name" : name})

    def upItemList(self,ID,name,change):
        #name = input("Enter name for update:")
        #name1=input("Enter new price")
        print(ID,name,change)
        self.collectionShopListItemt.update_one({"id":ID},{"$set": {str(name):change}})

    def delAllItemList(self):        
        self.collectionShopListItemt.delete_many({})

   