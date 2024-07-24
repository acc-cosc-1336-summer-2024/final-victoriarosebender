#add import

import question_c


def menu():
    print("Final Exam Menu \n 1-List Analysis \n 2-Exit")
    ##this is the menu




        
def run_menu(choice):        
    if (choice == '1'):
        max_list = 5 
        counter = 0
        my_list = []

        print("Enter a 5 integer list.")
        while(counter < max_list):
            num = input("Enter an integer: ")
            num = int(num)
            my_list.append(num)
            counter += 1
        question_c.data_analysis(my_list) 

        
        
    

    elif (choice == '2'):
        print('Exiting')

    else:
        print('Invalid Input')

def user_controlled_loop(): 
    choice = '1'
       
    while( choice != '2'):
        menu()
        choice = input("Enter Menu Option: ")
        run_menu(choice)




user_controlled_loop()