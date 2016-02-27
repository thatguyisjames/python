# simple text adventure
import os
os.system('clear')
print("Welcome to the cave entrance.")
print("My name is Doug, I'm the tour guide.")
name = raw_input("Whats your name stranger? ")
os.system('clear')
print("well %s, I'm happy you are here to explore with me") % (name)
print("at any time type \"help\" for commands")
print("lets get started!")
print("Go ahead a type \"forward\" and we will enter the cave")
