from Request import *
from Recipe import *

dashes = '-'* 30
RED = "\033[31m"
RESET = "\033[0m"  # Reset to default color


def print_mainMenu():
    print(dashes)
    print("\t Main Menu")
    print(dashes)
    print("1 - List all Categories")
    print("2 - List all meals by category")
    print("3 - Search Meal")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - List all Meal by Area")
    print("7 - Exit")
    print(dashes)
    
    

# list all categories
def opt1():
    print("{}\nList all Categories\n{}".format(dashes, dashes))
    categories = getCategories()
    for i in categories:
        print(i)
    print(dashes)
    
    # user search meal or return to main menu
    option = list_helper("category")
    if option: 
        user_input = input(f"Select number of area you've chosen (1-{len(categories)}): ")
        #TODO error handling
        opt2_helper(categories[int(user_input) - 1])
    else:
        # returns to Main Menu
        return
    
# list all meals by category
def opt2_helper(category: Category):
    print(f"{dashes}\nAll meals in {category.get_name()} \n{dashes}")
    meals = meal_by_category(category.name)
    for i in meals:
        print(i)
    print(dashes)
    
def opt2():
    # list categories
    print("{}\nList all Categories\n{}".format(dashes, dashes))
    categories = getCategories()
    for i in categories:
        print(i)
    print(dashes)
    
    # catch error user selection of meal
    while True:
        try:
            user_input = int(input(f"Enter number (1-{len(categories)}): "))
            # user error input 1-{len(areas)}
            if user_input > 0 and user_input <= len(categories):
                user_category = categories[user_input - 1]
                break
            else:
                print(RED + "Error" + RESET, end = ": ")
            
        except ValueError:
            print(RED + "Error" + RESET, ": Invalid input. Please enter a number.")
            
        
    opt2_helper(user_category)
    search_meal()

# random meal
def opt4():
    print("{}\nRandom Meal\n{}".format(dashes, dashes))
    print(random_meal())
    print(dashes)

# list areas
def opt5():
    print("{}\nList all Areas\n{}".format(dashes, dashes))
    areas = get_areas()
    count = 1
    for i in areas:
        print(f"{count} - {i}")
        count += 1
    print(dashes)
    
    # user search meal or return to main menu
    option = list_helper("area")
    if option: 
        user_input = input(f"Select number of area you've chosen (1-{len(areas)}): ")
        #TODO error handling
        opt6(areas[int(user_input) - 1])
    else:
        # returns to Main Menu
        return

# list all meals in area
def opt6(area):
    print(f"{dashes}\nAll meals in {area} \n{dashes}")
    meals = meal_by_area(area)
    for i in meals:
        print(i)
    print(dashes)
    
def opt6_helper():
    # list areas
    print("{}\nList all Areas\n{}".format(dashes, dashes))
    areas = get_areas()
    count = 1
    for i in areas:
        print(f"{count} - {i}")
        count += 1
    print(dashes)
    
    # catch error user selection of meal
    while True:
        try:
            user_input = int(input(f"Enter number (1-{len(areas)}): "))
            # user error input 1-{len(areas)}
            if user_input > 0 and user_input <= len(areas):
                user_area = areas[user_input - 1]
                break
            else:
                print(RED + "Error" + RESET, end = ": ")
            
        except ValueError:
            print(RED + "Error" + RESET, ": Invalid input. Please enter a number.")
            
        
    opt6(user_area)
    search_meal()
    
    
# search meal by name, returns meal object if successful
def search_meal_name() -> Meal:
    print("{}\nSearch Meal by Name\n{}".format(dashes, dashes))
    user_input = input("Search: ")
    user_meal = meal_by_name(user_input)
    # meal does not exist
    if not user_meal:
        print(RED + "Error" + RESET + ": Unable to find meal")
        return False
    # if search returns only 1 meal
    elif len(user_meal) == 1:
        return user_meal[0]
    # if search returns a list of meals
    else:
        # list meals
        counter = 1
        while counter <= len(user_meal):
            print(f"{counter} - {user_meal[counter - 1].name}")
            counter += 1
        
        # catch error user selection of meal
        while True:
            try:
                user_input = int(input(f"Enter number (1-{len(user_meal)}): "))
                # user error input 1-{len(user_meal)}
                if user_input >= 1 and user_input <= len(user_meal):
                    return user_meal[user_input - 1]
                else:
                    print(RED + "Error" + RESET, end = ": ")
                
            except ValueError:
                print(RED + "Error" + RESET, ": Invalid input. Please enter a number.")
                
        

# search meal by id number, returns meal object if successful
def search_meal_id() -> Meal:
    print("{}\nSearch Meal by Number\n{}".format(dashes, dashes))
    while True:
        try:
            user_input = int(input("Search: "))
            break
        except ValueError:
            print(RED + "Error" + RESET, ": Invalid input. Please enter a number.")
    
    user_meal = meal_by_id(user_input)
    # catch invalid number
    if not user_meal:
        print(RED + "Error" + RESET + ": Unable to find meal")
        return False
    else:
        return user_meal


def search_meal() -> str: 
    """ 
        Allows user to search by number or name, return None if select MainMenu
        if user searches sucessfully they can see recipe or return to MainMenu
    """
    is_error = "SEARCH MEAL"
    while True:
        print(dashes)
        print("\t", is_error)
        print(dashes)
        print("1 - search meal by number")
        print("2 - search meal by name")
        print("3 - return to Main Menu")
        print(dashes)
        user_input = input("Please select a number (1-3): ")
        if(user_input == '1'):
            meal = search_meal_id()
            if meal:
                break
        elif(user_input == '2'):
            meal = search_meal_name()
            if meal:
                break
        elif(user_input == '3'):
            return
        else:
            is_error = RED + "ERROR" + RESET
            
    meal = Recipe(meal)
    meal.show_recipe()
        

def list_helper(x):
    """ list area/category helper"

    Args:
        x (str): "area" or "category"

    Returns:
        boolean: True: search meal by area/category, False: return to MainMenu
    """
    print("\tSELECTION")
    print(dashes)
    print(f"1 - search meal by {x}")
    print("2 - return to Main Menu")
    print(dashes)
    
    while True:
        user_input = input("Please select a number (1 or 2): ")
        if(user_input == '1'):
            return True
        elif(user_input == '2'):
            print_mainMenu()
            return False
        else:
            print(RED + "Error:" + RESET, end=" ")

def recipe_selection(meal: Meal):
    print(dashes)
    print("\tSELECTION")
    print(dashes)
    print(f"1 - see meal recipe?")
    print("2 - return to Main Menu")
    print(dashes)
    
    while True:
        user_input = input("Please select a number (1 or 2): ")
        if(user_input == '1'):
            print(dashes)
            recipe = Recipe(meal)
            recipe.show_recipe()
            return
        elif(user_input == '2'):
            return
        else:
            print(RED + "Error:" + RESET, end=" ")
            