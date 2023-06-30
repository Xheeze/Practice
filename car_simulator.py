#!/usr/bin/python3

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
       if started == True:
        print("vehicle already Started")
       else:
        started == True
        print("Car is warming up")    
    elif command == "stop":
        if not started == True:
          print("Vehicle engine is already offline")
        else:
          started == False
          print("Turning engine off")
    elif command != "help":
        print("I didn't understand that")        
        input('''
start:: to start the car
stop:: to stop the car
quit:: to terminate the simulation''')
    
    elif command == "quit":
      print("Closing simulator")
      print(".............................")
      break
