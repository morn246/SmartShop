

from sys import exit

def menu(C):    
    while True:        
        print("\n choose a number [1-7]: \n"
        "\n", "[1] View the current shopping list", 
        "\n", "[2] Add another item to the list",        
        "\n", "[3] Update the price of a particular item",        
        "\n", "[4] Delete the item", 
        "\n", "[5] Update the budget of the shopping list", 
        "\n", "[6] Diagram of budget per month",
         "\n", "[7] Who is the most wasteful user?",
        "\n",  "[8] Exit","\n") 
        
        try:
            chose= int(input())  
            if(1== chose):
                C.printList()
            elif(2== chose):
                C.addItemList()
            elif(3== chose):
                C.upItemList()
            elif(4== chose):
                C.delItemList()
            elif(5== chose):
                C.createL()
            elif(6== chose):
                year= input("Enter year for budget diagran:")
                C.clacBudget(year)
            elif(7== chose):  
                 C.whoIsWasteful()
            elif(8== chose):
                print("Logout.... ")
                exit(0)
        except Exception as e:
            print("An exception occurred ",e) 
     
                        














