#!/usr/bin/python3

i = 0
restu = [
    "RocoMammas",
    "Spur",
    "Nandos",
    "Grillos"
   ]
symbols= {
    "state_bird" : "California quail",
    "state_animal" : "Grizzly bear",
    "state_flower" : "California poppy",
    "state_fruit" : "Avocado"}
while i < 6:
    print("~\ " * i,"\n")
    i += 1
    #print(restu[i]) #,symbols[i]
while i > 1:
    i -= 1
    print("~/ " * i,"\n")
    #print(symbols[i])
print("\nDone!")

person = {
    "name":"Sunita",
    "":"211-555-5471",
    "address":["1247 Ellof Street","Johannesburg"]
}
print(person["address"][1])
item1 =[1,2,3,4]
item2 = {'a':1, 'b':2, 'c':3, 'd':4}
print(item1[2] + item2['c'])

# Fruit class for red apple
class Fruit():
    def __init__(self,color):
        self.color = color
    def describe(self):
        print(self.color)
Apple = Fruit('red')
Apple = Fruit('green')
Apple.describe()
#Fruit.describe()
#Apple.describe('red')
Fruit.describe(Apple)

#loop
# counter = 0
# target = 10
# while counter< target:
#     print(counter)
#     target+=1

num = input('your number? ')
print('yournumber sqrd iz',num*4)

value = 1
count = 0
while value<20:
    value += 4
    count += 1
print("reached",value,"after",count,"iterations")