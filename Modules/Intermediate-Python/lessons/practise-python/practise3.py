class MyFirstClass:
    num = 12345
    def greet(self):
        return "Hello World"
    
number = MyFirstClass()

# print(number.num)
# print(number.greet())

# class House:
#     layout = "square"
#     def paint(self, colour):
#         self.colour = colour
        
# home = House()
# print(type(home))

# home.size = "1000"


# home.num_bathrooms = 2
# home.num_bedrooms = 3
# home.colour = "Blue"
# print(home.__dict__["size"])

# class House:
#     def __init__(self, size, colour="white"):
#         self.size = size
#         self.colour = colour
        
# home = House(1000)
# print(home.colour)

class House:
    layout = 'square'
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
    def paint(self, color):
        self.color = color
        
home = House(1000)
# print(home.size)
# print(home.color)
home.paint("red")
print(home.paint("red"))