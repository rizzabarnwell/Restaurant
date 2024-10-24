class Category:
    def __init__(self, id, name, description) -> None:
        self.id = id
        self.name = name
        self.description = description
        
    def __str__(self):
        return f'{self.id} - {self.name}'
    
    def get_name(self):
        return self.name
    
