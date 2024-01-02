'''
Mineral Water
Jimmy is a truck driver who delivers mineral water. He loads the water from a warehouse and distributes it
 within many stores in the town. Sometimes when Jimmy goes to the warehouse there is not enough water to full
 the truck which makes him angry. He wants to go for delivery only if the truck is full.

You can help him if you write a program that checks if it is possible to load the whole truck.

The mineral water is available in two types of bottles - 1 liter and 5 liters. Jimmy always tries to
load as much of the big bottles first and then adds small bottles. Given the capacity of the truck and
the available bottles in the warehouse you should calculate the number of
small bottles that he will load. If there are not enough small bottles the result should be -1.
'''

# smallb = 6
# bigb = 3
# truck_capacity = 15
smallb, bigb, truck_capacity = int(input()), int(input()), int(input())
substraction = truck_capacity - bigb * 5
capacity_left_for_smallb = substraction % 5 if substraction < 0 else substraction
if capacity_left_for_smallb - smallb <= 0:
    print(capacity_left_for_smallb)
else:
    print(-1)
