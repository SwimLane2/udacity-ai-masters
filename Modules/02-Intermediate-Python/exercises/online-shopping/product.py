class Product:
    def __init__(self, name, description, seller, price):
        self.name = name
        self.description = description
        self.seller = seller
        self.price = price
        self.reviews = []
        self.available = True
        
    def __str__(self):
        return f"Product({self.name}, ${self.price})"