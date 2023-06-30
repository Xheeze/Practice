#!/usr/bin/python3

###### Temperature App
temp=int(input("What's the temperature in degrees?: "))
if temp < 12:
    is_hot=False
    if is_hot:
        print("get some sunscreen")
elif temp > 19:
    is_hot=True
    is_cold = False
else:
    print("Put on a jacket")
print("Relax and Have a great day!")