import View 
import ShopClass
from Model import ConnectionDB


class IController:
    def __init__(self):
        self.Con=ConnectionDB()
        View.menu(self.Con)
    def printList(self):
        self.Con.printList()
    def addItemList(self):
         self.Con.addItemList()
    def upItemList(self):
         self.Con.upItemList()
    def delItemList(self):
        self. Con.delItemList()
    def createL(self):
        s=ShopClass.ShoppList(self.Con)               
        self.Con.createList(s)
    def clacBudget(self,year):     
          self.Con.calBudgetPerMonth(year)
    def whoIsWasteful(self):
        self. Con.whoIsWasteful()




#running controller function
IController()
