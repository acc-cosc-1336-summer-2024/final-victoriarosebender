#add import

import question_a



def menu():
    print("Homework 7 Menu \n 1-Display stock purchase history \n 2-Exit")
    ##this is the menu




        
def run_menu(choice):        
    if (choice == '1'):
        stock = question_a.Stock("MSFT", "Microsoft") ###input values here

        stock.stock_purchase_history()

        
        
    

    elif (choice == '2'):
        print('Exiting')

    else:
        print('Invalid Input')

def user_controlled_loop(): 
    choice = 1  
    while( choice != '2'):
        menu()
        choice = input("Enter Menu Option: ")
        run_menu(choice)




user_controlled_loop()