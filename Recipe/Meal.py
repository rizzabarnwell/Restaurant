class Meal:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        
    def __str__(self):
        return f'{self.id} - {self.name}'
    
    def get_meal_id(self):
        return self.id