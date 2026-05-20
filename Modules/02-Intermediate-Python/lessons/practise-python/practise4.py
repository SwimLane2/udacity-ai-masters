# class MotorVehicle:
#     def __init__(self, range):
#         self.range = range
#         self.tank = range
#     def travel(self, distance):
#         if distance > self.tank:
#             print(f"Not enough in the tank. Only traveled {self.tank} kilometers.")
#             self.tank = 0
#         else:
#             print(f"VOOOM! Traveled {distance} kilometers.")
#             self.tank -= distance
#     def refuel(self):
#         print("Refueling...")
#         self.tank = self.range
#     def __str__(self):
#         return(f"Vehicle(range={self.range}, tank={self.tank})")
    
# class Car(MotorVehicle):
#     def __init__(self, range, wheels, colour):
#         super().__init__(range)
#         self.wheels = wheels
#         self.colour = colour

            

# mv = MotorVehicle(100)
# print(mv)
# mv.travel(50)  # VOOOM! Traveled 50 kilometers.
# mv.travel(30)  # VOOOM! Traveled 30 kilometers.
# mv.travel(20)  # Not enough in the tank. Only traveled 20 kilometers.
# print(mv)
# mv.refuel() 
# print(mv)
# c = Car(500, 4, 'red')



import math
help(math)