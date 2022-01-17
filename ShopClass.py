# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:08:25 2021

@author: 97252
"""
import datetime 
import itertools
import enum
  
# creating enumerations using class
class ShopEnu(enum.Enum):
    ID=0
    date = 1
    name = 2
    price = 3
    quantity=2
    user=5
    Det=6
    ShoppingDate=7
    isDone=8
    
class ShoppList:
     _ID=1
     def __init__(self, Con):
         self.id = self._ID 
         self.__class__._ID += 1
         self.Con=Con
         self.collectionShopListItemt=Con.collectionShopListItemt      
         self.shoppingDate=datetime.datetime.now()
         self.ListShop=self.ListShopCurr()
         self.sumPrice= self.GetSumPrice()
         print("sy")
         self.actualPrice=int(input("Enter actual price just numbers:"))    
         self.updateDoneshoppingDate()
         print("sm")
         
     def ListShopCurr(self):
          List=[]
          res=self.collectionShopListItemt.find({"isDone":False})
          for shopItem in res:
              #print(shopItem["name"], shopItem["price"])
              #shopItem={shopItem["_id"],shopItem["date"],shopItem["name"],shopItem["price"],shopItem["quantity"],shopItem["user"],shopItem["Det"],shopItem["ShoppingDate"],shopItem["isDone"]}  
              List.append(shopItem)
          return List
              
     def updateDoneshoppingDate(self):
        for s in self.ListShop:           
             s["ShoppingDate"]=self.shoppingDate
             s["isDone"]=True 
             print("nn")
             self.Con.upItemList(s["_id"],"isDone",True)
             self.Con.upItemList(s["_id"],"ShoppingDate",self.shoppingDate)
             print("mmm")
         
     def GetSumPrice(self):
         sum1=0
         for s in self.ListShop:
             print(s["price"])
             sum1+=float(s["price"])
             
         return sum1   


    
class ShopListItem: 
  _ID=1
  def __init__(self, user1):
         self.id = self._ID 
         self.__class__._ID += 1
         self.date= datetime.datetime.now()
         self.name=input("Enter name:")
         self.user=user1
         self.price=0
         self.quantity=1
         self.isDone=False 
         self.shoppingDate=None
  


    


class User: 
    
    _ID=1
    def __init__(self):
        self.id = self._ID 
        self.__class__._ID += 1
       
        self.name="מור"#input("Enter name user:")
        self.passw="123"#input("Enter name password:")
                  

    def addUser(self,Con):
        
        u={"name":self.name,"passw":self.passw,"id":self.id}
        Con.collectionUser.insert_one(u)
            
 
