#!/bin/env python3

 # The player begins with 100 health points
health_points = 100

def showInstructions():
    # Print a main menu and the commands
    print("Welcome to the Royal Palace Adventure Game!")
    print("=========")
    print("Commands:")
    print("'go [direction] 'north', 'east', 'south', 'west';")
    print( "'south-east', 'south-west', 'north-east', or 'north-west'")

"""Shows all possible directions from all rooms"""
#def show_directions():
    #for room in available_rooms.values():
       # print(room["name"])
       # print(room["directions"])

"""Shows all possible directions from current room"""
def show_directions(currentRoom):
    print("These are the available directions: ")
    print(available_rooms[currentRoom]["directions"])

"""Shows the enemy in the current room"""
def show_enemies(currentRoom):
    print("")
    print("There is an enemy in this room! It is a ")
    print(enemies[currentRoom]["type"])
    print("Do you wish to attack or flee?")

"""Prints the player's current status"""
def showStatus():
    # Print the player's current status
    print("-------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    print("--------------------")

# The magic bag stores all kinds of items, but is empty at the start
magicBag = []

# Start the player in room 1
currentRoom = 1

showInstructions()

def addToMagicBag(item):
    magicBag.append(item)

def addToMagicBag2(room_items):
    magicBag.append(room_items)

#def pickUpItem():
#    pickup = input()
#    if pickup == "yes":
#        addToMagicBag(item)
 #   else:
 #       print("Leave item on the floor")


#def startRoom():

"""Show the items in the current room"""
def show_items(currentRoom):
    print("")
    print("This is the item you find in the room:")
    print(room_items[currentRoom]["items"])
    print("Would you like to pick it up?")

def pick_up_item(currentRoom):
    pickup = input("> yes or no")
    if pickup == "yes":
        #item = room_items[currentRoom]["items"][0] #single item is sword
        #magicBag.append(item) #adds sword to magic bag
        #room_items[currentRoom]["items"].remove(item) # removes sowrd from room

        for item in room_items[currentRoom]["items"]:
            magicBag.append(item)
        #magicBag.append(room_items[currentRoom]["items"]) # This will cause duplication
        print(magicBag)

def attack(currentRoom): # I NEED WORK ON THIS!!!
    attack = input("> attack/ do nothing")
    if attack == "attack":
        print("Select the weapon or spell you wish to use to attack")
    item_used = input(">")
    if item_used in magicBag: # if item is in magicBag then use it to attack the enemy
        print("your enemy has been defeated")
    else:
        print("You do not own this item.")
        print(magicBag)

# Loop infinitely
while True:

    showStatus()
    show_directions(currentRoom)
    #startRoom()

    if room_items[currentRoom]["items"] != []:
      show_items(currentRoom)
      pick_up_item(currentRoom)
    if enemies[currentRoom]["type"] != []:
      show_enemies(currentRoom)
      attack(currentRoom)

    # Get the player's 'move'
    # Split() breaks it up into a list array
    # eg Typing 'go east' would give the list:
    # ['go', 'east']
    move = input(">").lower().split()

    # If they type 'go' first
    if move[0] == "go":
        # Check that they are allowed wherever they want to go
        if move[1] in rooms [currentRoom]:
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # There is no door (link) to the new room
        else:
            print("You can't go that way!")