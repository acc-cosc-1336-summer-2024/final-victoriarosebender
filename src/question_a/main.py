#add import

import question_a



def menu():
    print("Final Exam Menu \n 1-Display stock purchase history \n 2-Exit")
    ##this is the menu




        
def run_menu(choice):        
    if (choice == '1'):
        

        question_a.stock_purchase_history()

        
        
    

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