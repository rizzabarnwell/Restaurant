import requests
from Category import Category
from Meal import Meal

# API base URL
BASE_URL = "https://www.themealdb.com/api/json/v1/1"

def meal_recipe(meal_id):
    """
    return json file of given meal
    """
    url = f'{BASE_URL}/lookup.php?i={meal_id}'
    r = requests.get(url)
    return r.json()
    

def getCategories():
    """
    Get all meal categories from themealdb, returns a list of Category objects
    """
    url = f'{BASE_URL}/categories.php'
    r = requests.get(url)
    categories = []
    
    if r.status_code == 200:
        json = r.json()
        for c in json['categories']:
            category = Category(c['idCategory'], c['strCategory'], c['strCategoryDescription'])
            categories.append(category)
    else:
        print("Error")
        
    return categories
    
def meal_by_category(category):
    """
    Get all meals under a category, returns a list of Meal objects
    """
    url = f'{BASE_URL}/filter.php?c={category}'
    r = requests.get(url)
    meals = []
    
    if r.status_code == 200:
        json = r.json()
        for c in json['meals']:
            meal = Meal(c['idMeal'], c['strMeal'])
            meals.append(meal)
    else:
        print("Error")
        
    return meals

def meal_by_name(meal):
    """
    takes search as argument, returns Meal object or False if Meal doesnt exist
    """
    #TODO handle multiple meals returned
    url = f'{BASE_URL}/search.php?s={meal}'
    r = requests.get(url)
    
    if r.status_code == 200:
        json = r.json()
        if json['meals'] == None:
            return False
        else:
            meals = []
            for c in json['meals']:
                meal = Meal(c['idMeal'], c['strMeal'])
                meals.append(meal)
            return meals


def random_meal():
    """
    returns a random meal object
    """
    url = f'{BASE_URL}/random.php'
    r = requests.get(url)
    
    if r.status_code == 200:
        json = r.json()
        meal = Meal(json['meals'][0]['idMeal'], json['meals'][0]['strMeal'])
    else:
        print("Error")
    
    return meal


def get_areas():
    """
    Get all meal areas from themealdb, returns a list 
    """
    url = f'{BASE_URL}/list.php?a=list'
    r = requests.get(url)
    areas = []
    
    if r.status_code == 200:
        json = r.json()
        for c in json['meals']:
            areas.append(c['strArea'])
    else:
        print("Error")
        
    return areas

def meal_by_area(area):
    """
    Get all meals under an area, returns a list of Meal objects
    """
    url = f'{BASE_URL}/filter.php?a={area}'
    r = requests.get(url)
    meals = []
    
    if r.status_code == 200:
        json = r.json()
        if(json['meals'] == None):
            return False
        else:
            for c in json['meals']:
                meal = Meal(c['idMeal'], c['strMeal'])
                meals.append(meal)
    else:
        print("Error")
        
    return meals

def meal_by_id(id):
    """
    takes search as argument, returns Meal object or false if meal does not exist
    """
    url = f'{BASE_URL}/lookup.php?i={id}'
    r = requests.get(url)
    
    if r.status_code == 200:
        json = r.json()
        if json['meals'] == None:
            return False
        else:
            meal = Meal(json['meals'][0]['idMeal'], json['meals'][0]['strMeal'])
    else:
        print("Error")
        
    return meal