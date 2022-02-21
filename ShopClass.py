# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:08:25 2021

@author: 97252
"""
import datetime 
import itertools
from sys import exit

    
class ShoppList:
     #__slots__='Con','collectionShopListItem','actualPrice','id','ListShop','sumPrice','shoppingDate'
     def __init__(self, Con):
         self.Con=Con
         self.collectionShopListItem=Con.collectionShopListItem 
         self.ListShop=self.ListShopCurr()
         self.IsEmpty()
              
         self.id = id(datetime.datetime.now())
        
         self.shoppingDate=datetime.datetime.now()#"2021-05-05 10:10:10"
         self.sumPrice= self.GetSumPrice()
         self.actualPrice=int(input("Enter actual price just numbers:")) 
         self.updateDoneshoppingDate()
         
     def ListShopCurr(self):
          List=[]
          res=self.collectionShopListItem.find({"isDone":False})
          for shopItem in res:
              #print(shopItem["name"], shopItem["price"])
              #shopItem={shopItem["_id"],shopItem["date"],shopItem["name"],shopItem["price"],shopItem["quantity"],shopItem["user"],shopItem["Det"],shopItem["ShoppingDate"],shopItem["isDone"]}  
              List.append(shopItem)
          return List
    
     def IsEmpty(self): 
         try:
            
             if(self.ListShop.__len__()>0):
                 return False
             raise "no items in shoppingList"
         except Exception as e:
            print("Error  \n ", "no items in shoppingList")
            raise "no items in shoppingList"
            
         
     def updateDoneshoppingDate(self):
        
        for s in self.ListShop:           
             s["ShoppingDate"]=self.shoppingDate
             s["isDone"]=True 
            
             self.Con.upItemList1(s["id"],"isDone",True)
             self.Con.upItemList1(s["id"],"ShoppingDate",self.shoppingDate)

         
     def GetSumPrice(self):
         totalSum=0
         for s in self.ListShop:
             totalSum+=float(s["price"])             
         return totalSum   


    
class ShopListItem: 
  #__slots__='id','date','name','user','quantity','isDone','shoppingDate','price'
  def __init__(self, user1):
         self.id = id(datetime.datetime.now())
         self.date=datetime.datetime.now() #"2021-5-5 10:10:10"#
         self.name=input("Enter name item for shopping list:")
         self.user=user1
         self.price=0
         self.quantity=1
         self.isDone=False 
         self.shoppingDate=None
  

class User: 
    #__slots__='id','name','passw'   
    def __init__(self):
        self.id = id(datetime.datetime.now())
        self.name=input("Enter name user:")
        self.passw=input("Enter name password:")
                  

    def addUser(self,Con):       
        u={"id":self.id,"name":self.name,"passw":self.passw}
        Con.collectionUser.insert_one(u)
            
 
