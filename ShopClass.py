# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:08:25 2021

@author: 97252
"""
import datetime 
import itertools
# import enum
  
# # creating enumerations using class
# class ShopEnu(enum.Enum):
#     ID=0
#     date = 1
#     name = 2
#     price = 3
#     quantity=2
#     user=5
#     Det=6
#     ShoppingDate=7
#     isDone=8
    
class ShoppList:

     def __init__(self, Con):
         self.id = id(datetime.datetime.now())

         self.Con=Con
         self.collectionShopListItem=Con.collectionShopListItem      
         self.shoppingDate=datetime.datetime.now()
         self.ListShop=self.ListShopCurr()
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
              
     def updateDoneshoppingDate(self):
        for s in self.ListShop:           
             s["ShoppingDate"]=self.shoppingDate
             s["isDone"]=True 
             self.Con.upItemList(s["name"],"isDone",True)
             self.Con.upItemList(s["name"],"ShoppingDate",self.shoppingDate)

         
     def GetSumPrice(self):
         totalSum=0
         for s in self.ListShop:
             totalSum+=float(s["price"])             
         return totalSum   


    
class ShopListItem: 

  def __init__(self, user1):
         self.id = id(datetime.datetime.now())
         self.date= datetime.datetime.now()
         self.name=input("Enter name:")
         self.user=user1
         self.price=0
         self.quantity=1
         self.isDone=False 
         self.shoppingDate=None
  

class User:     
    def __init__(self):
        self.id = id(datetime.datetime.now())
        self.name=input("Enter name user:")
        self.passw=input("Enter name password:")
                  

    def addUser(self,Con):       
        u={"name":self.name,"passw":self.passw,"id":self.id}
        Con.collectionUser.insert_one(u)
            
 
