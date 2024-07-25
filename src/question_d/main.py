#add import
import question_d

def menu():
    print("Final Exam Menu \n 1-Create Multiplication Table \n 2-Exit")
    ##this is the menu




        
def run_menu(choice):        
    if (choice == '1'):
        
        rows = input("Input desired multiples rows: ")
        cols = input("Input desired multiples columns: ")

        
        my_list = question_d.create_mulitiplication_table(rows,cols)

        question_d.display_multiplication_table(my_list)

        
        
    

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