class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []
        
    def __str__(self):
        return f"User({self.id}, {self.name})"
    
    def sell_product(self, name, description, price):
        from product import Product
        return Product(name, description, self, price)

    def buy_product(self, product):
        product.available = False

    def write_review(self, description, product):
        from review import Review

        review = Review(description, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review

brianna = User(1, 'Brianna')
mary = User(2, 'Mary')
keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True
