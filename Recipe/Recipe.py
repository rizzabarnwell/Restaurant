from Meal import Meal
from Request import meal_recipe

class Recipe(Meal):
    def __init__(self, meal: Meal) -> None:
        self.id = meal.get_meal_id()
        
        json = meal_recipe(self.id)
        
        self.name = json['meals'][0]['strMeal']
        self.category = json['meals'][0]['strCategory']
        
        # format instructions
        self.instructions = json['meals'][0]["strInstructions"]
        
        # create dictionary of meal ingredients and measures
        i = 1
        ingredients = {}
        while i <= 20:
            ingredient = json['meals'][0][f'strIngredient{i}']
            #check for end of the ingredients listed in json 
            if ingredient == None or len(ingredient) == 0:
                break
            # add measurements of given ingredient
            measurement = json['meals'][0][f'strMeasure{i}']
            ingredients[ingredient] = measurement
            i += 1
        self.ingredients = ingredients
            

        
    def show_recipe(self):
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Category: ", self.category)
        # #format
        print("Ingredients:")
        for keys, value in self.ingredients.items(): 
            print(f"\t{value} {keys}")
        # format
        print("Instructions:\n\n",self.instructions)     
        """TODO
        self.instructions = self.instructions.split(".")
        
        for i in self.instructions:
            if i.startswith("\r"):
                print("x")
                i.removeprefix("\r\n") 
                print(repr(i))
            print(f"\t- {repr(i)}")
        """