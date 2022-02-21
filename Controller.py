import View 
import ShopClass
from Model import ConnectionDB


class IController:
    def __init__(self):
        self.Con=ConnectionDB()
        View.menu(self)
    def printList1(self):
        self.Con.printList()
    def addItemList1(self):
         self.Con.addItemList()
    def upItemList1(self):
         self.Con.upItemList()
    def delItemList1(self):
        self.Con.delItemList()
    def createL1(self):
        s=ShopClass.ShoppList(self.Con)               
        self.Con.createList(s)
    def clacBudget1(self,year):     
          self.Con.calBudgetPerMonth(year)
    def whoIsWasteful(self):
        self. Con.whoIsWasteful()




#running controller function
IController()
