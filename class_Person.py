#!/usr/bin/python3

class Person:
	def __init__(self,name):
		self.name = name
	
	def talk(self):
		print(f'{self.name}, can talk.')

john = Person('John')
#john.talk()

bob = Person('Bobby V')
#bob.talk()

#inheritance starts
class Android(Person):
	pass
	def lavitate(self):
		print("watch me float and _shift_")

droid = Android('Lloyd now')
droid.talk()
droid.lavitate()
