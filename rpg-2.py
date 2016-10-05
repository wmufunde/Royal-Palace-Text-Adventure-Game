#!/bin/env python3

from Map import *

 # The player begins with 100 health points
health_points = 100

def showInstructions():
    # Print a main menu and the commands
    print("Welcome to the Royal Palace Adventure Game!")
    print("=========")
    print("Commands:")
    print("'go [direction] 'north', 'east', 'south', 'west';")
    print( "'south-east', 'south-west', 'north-east', or 'north-west'")

"""Shows all possible directions from current room"""
def show_directions(currentRoom):
    print("These are the available directions: ")
    print(list(rooms[currentRoom].keys()))

"""Shows the enemy in the current room"""
def show_enemies(currentRoom):
    print("")
    print("There is an enemy in this room! It is a ")
    print([e.name for e in currentRoom.enemies])
    print("Do you wish to attack or flee?")

"""Prints the player's current status"""
def showStatus():
    # Print the player's current status
    print("-------------------")
    print("You are in the " + currentRoom.name)
    print("-------------------")
    print("You have " + str(health_points) + " Health Points.")

# The magic bag stores all kinds of items, but is empty at the start
magicBag = []

# Start the player in room 1
currentRoom = ballroom

showInstructions()

def addToMagicBag(item):
    if item not in magicBag:
        magicBag.append(item)

"""Show the items in the current room"""
def show_items(currentRoom):
    print("")
    print("This is the item you find in the room:")
    print(currentRoom.items)
    print("Would you like to pick it up?")

def pick_up_item(currentRoom):
    pickup = input("> yes or no")
    if pickup == "yes":

        for item in currentRoom.items:
            addToMagicBag(item)
            #magicBag.append(item)
        print(magicBag)

"""Allows the player to use an item in the magic bag to attack a creature"""
def attack(currentRoom): # I NEED WORK ON THIS!!!
    attack = input("> attack/ do nothing")
    if attack == "attack":
        print("Select the weapon or spell you wish to use to attack")
    item_used = input(">")
    if item_used in magicBag: # if item is in magicBag then use it to attack the enemy
        for enemy in currentRoom.enemies:
            if item_used == "sword":
                enemy.health -= 10
            if item_used == "crossbow":
                enemy.health -= 15
            if item_used == "shield":
                enemy.health -= 5
            if item_used == "super speed spell":
                enemy.health -= 15
            if item_used == "lightning spell":
                enemy.health -= 30
            if item_used == "freezing spell":
                enemy.health -= 20
            if item_used == "invisibility spell":
                enemy.health -= 5

        print("The enemy has " + str ([e.health for e in currentRoom.enemies])+ " health points left")

        #print("your enemy has been defeated")
        if item_used not in reusable_items:
            magicBag.remove(item_used)
    else:
        print("You do not own this item.")
        print(magicBag)

def be_attacked(currentRoom):
    for enemy in currentRoom.enemies:
        global health_points
        currentRoom.enemies
        if enemy == "dark elf":
            health_points -= 20
        if enemy == "goblin":
            health_points -= 7
        if enemy == "harpy":
            health_points -= 30
        if enemy == "malignant spirit":
            health_points -= 15

# Loop infinitely
while True:

    #health_points -= 50

    showStatus()

    if health_points <= 0:
        print("Game Over!")
        break


    show_directions(currentRoom)
    #startRoom()

    if currentRoom.items != []:
      show_items(currentRoom)
      pick_up_item(currentRoom)
    if currentRoom.enemies != []:
      show_enemies(currentRoom)
      attack(currentRoom)
      be_attacked(currentRoom)

    # Get the player's 'move'
    # Split() breaks it up into a list array
    # eg Typing 'go east' would give the list:
    # ['go', 'east']
    move = input(">").lower().split()
    command = move[0]

    # If they type 'go' first
    if command == "go" and len(move) is 2:
        direction = move[1]
        # Check that they are allowed wherever they want to go
        if direction in rooms[currentRoom]:
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][direction]
        # There is no door (link) to the new room
        else:
            print("You can't go that way!")