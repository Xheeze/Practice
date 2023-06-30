#!/usr/bin/python3

############ Mortgage Calculator ###############

House = 10000000.00 
credit = input("How's your credit: Good or Bad? ") #user prompt
payment = 10 #rubbish  value to initialize credit variable
if credit == "Good":
    good_credit = True
elif credit == "Bad":
    good_credit = False
    
if good_credit:  #credit rating for payment options
	payment = House * .1
    
else:
	payment = House * .2
balanco = float(House - payment) #Balance calculated
#
print(f'''\nYour down Payment: R{payment}
  and the Balance: R{balanco}''')