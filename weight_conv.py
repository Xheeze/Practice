#!/usr/bin/python3

###### Weight converter App
weight = int(input("Enter your Weight:"))
meausr= input("in (kg)s or (lb)s")
# Print the result of the conversion
if meausr == "kg":
    weight_in_pounds = weight /.4
    print("Well, you weigh",weight_in_pounds , "lbs")

elif meausr == "lb":
    weight_in_kilograms = weight *.45
    print("Well, you weigh",weight_in_kilograms, "kgs")