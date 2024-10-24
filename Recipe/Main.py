from MainMenu import * 

def main():
    print_mainMenu()
    while True:
        user_input = input("Please select a number (1-7): ")
        if(user_input == '1'):
            opt1()
            print_mainMenu()
        elif(user_input == '2'):
            opt2()
            print_mainMenu()
        elif(user_input == '3'):
            search_meal()
            print_mainMenu()
        elif(user_input == '4'):
            opt4()
            print_mainMenu()
        elif(user_input == '5'):
            opt5()
            print_mainMenu()
        elif(user_input == '6'):
            opt6_helper()
            print_mainMenu()
        elif(user_input == '7'):
            break
        else:
            print(RED + "Error" + RESET, end=": ")
            
            
if __name__ == "__main__":
    main()