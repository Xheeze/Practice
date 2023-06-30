#!/usr/bin/python3
from pyclbr import Class
# Class Puppy()
# def __init__(self,name,favourite_toy):
# 	self.name = name
# 	self.favourite_toy = favourite_toy
# #############################		
# def play(self):
# 	print(self.name + " is playing with the " + self.favourite_toy)
# ######################
# marble = Puppy('Marble', 'teddy bear')
# marble.play()
# ##############
# onyx =  Puppy('Onyx', 'lizard')
# onyx.play()

import random
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(numbers)
# print(numbers)
random.sample((numbers,6))