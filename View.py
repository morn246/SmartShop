
from sys import exit
"""
File View:
    Menu for management SmartShop
    renders presentation of the model 
"""
def mainMenu():
    while True:
        print("\n Click 1 to view reports or \n Click 2 Shopping Actions")
        chose= int(input())  
        if(chose==1):
            return 1
        if(chose==2):
            return 2
        print(" try again,")
     
def check(click,chose):
    if click==1:
        if chose==1 or chose==6 or chose==7 or chose==8:
            return True
    elif click==2:
        if chose==2 or chose==3 or chose==4 or chose==5 or chose==7 or chose==8:
            return True
    return False
        
def menu(C):
    flag= True    
    while True:
        if(flag):
            click= mainMenu()
            flag= False
        if(click==1):
            print("\n choose a number [1,6,7,8]: \n"
                  "\n", "[1] View the current shopping list",  
                  "\n", "[6] Diagram of budget per month",
                  "\n", "[7] Return to the main menu",
                  "\n", "[8] Exit","\n") 
        elif(click==2):
            print("\n choose a number [2,3,4,5,7,8]: \n"
                  "\n", "[2] Add another item to the list",        
                  "\n", "[3] Update the price of a particular item",        
                  "\n", "[4] Delete the item", 
                  "\n", "[5] Update the budget of the shopping list", 
                  "\n", "[7] Return to the main menu",
                  "\n", "[8] Exit","\n") 
        
        try:
            chose= int(input())
            if(check(click,chose)==False):
                print(" try again,")
                chose=9
                
            if(1== chose):
                C.printList1()
            elif(2== chose):
                C.addItemList1()
            elif(3== chose):
                C.upItemList1()
            elif(4== chose):
                C.delItemList1()
            elif(5== chose):
                C.createL1()
            elif(6== chose):
                year= input("Enter year for budget diagran:")
                C.clacBudget1(year)
            elif(7== chose):  
                 flag=True
            elif(8== chose):
                print("Exit from SmartShop.... ")
                exit(0)
        except Exception as e:
            print("An exception occurred ",e) 
     
                        














