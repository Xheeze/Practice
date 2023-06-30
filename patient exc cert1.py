#!/usr/bin/python3
name = input('patient name: ')
age = input(str('age: '))
new_patient = bool('New patient:')
colour = input("Blood type:")
sex = input("Gender:")
if new_patient == True:
    status = "NEW Patient"
else:
    status = "old Patient"
print(".................... \n","patient updated as:",name,",",age,"years old",sex,"withbloodtype:",colour)