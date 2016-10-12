#!/bin/env python3

 # The player begins with 100 health points
health_points = 100

"""Stores all possible directions from current room """

available_rooms = {1: {"directions": ["north", "east", "south"], "name": "Ballroom"},
                   2: {"directions": ["north-west", "north-east","south-west", "south-east"], "name": "Hallway"},
                   3: {"directions": ["south"], "name": "Female Bathroom"},
                   4: {"directions": ["north", "south"], "name": "Antechamber"},
                   5: {"directions": ["north"], "name": "Male Bathroom"},
                   6: {"directions": ["north"], "name": "Throne Room"},
                   7: {"directions": ["east", "south"], "name": "North Vestibule"},
                   8: {"directions": ["north", "east", "south"], "name": "South Vestibule"},
                   9: {"directions": ["north", "south", "west"], "name": "Blue Drawing Room"},
                   10: {"directions": ["north", "east", "south"], "name": "State Room"},
                   11: {"directions": ["north", "east", "west"], "name": "Hallway 2"},
                   12: {"directions": ["north-west", "north-east", "west", "north-west", "south-east"], "name": "Hallway 3"},
                   13: {"directions": ["east", "west"], "name": "Library"},
                   14: {"directions": ["west"], "name": "Gallery"}
                       }

enemies = {1: {"type": [], "name": "Ballroom"},
           2: {"type": [], "name": "Hallway"},
           3: {"type": [], "name": "Female Bathroom"},
           4: {"type": ["dark elf"], "name": "Antechamber"},
           5: {"type": [], "name": "Male Bathroom"},
           6: {"type": ["goblin"], "name": "Throne Room"},
           7: {"type": ["harpy"], "name": "North Vestibule"},
           8: {"type": [], "name": "South Vestibule"},
           9: {"type": ["malignant spirit"], "name": "Blue Drawing Room"},
           10: {"type": [], "name": "State Room"},
           11: {"type": ["goblin"], "name": "Hallway 2"},
           12: {"type": [], "name": "Hallway 3"},
           13: {"type": ["malignant spirit"], "name": "Library"},
           14: {"type": ["malignant spirit"], "name": "Gallery"}}

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


room_items = { 1: {"items": ["sword"], "name": "Ballroom"},
               2: {"items": ["crossbow"], "name": "Hallway"},
               3: {"items": ["pack of matches"], "name": "Female Bathroom"},
               4: {"items": [], "name": "Antechamber"},
               5: {"items": ["shield"], "name": "Male Bathroom"},
               6: {"items": [], "name": "Throne Room"},
               7: {"items": ["super speed spell."], "name": "North Vestibule"},
               8: {"items": ["lightning spell."], "name": "South Vestibule"},
               9: {"items": ["freezing spell."], "name": "Blue Drawing Room"},
               10: {"items": [], "name":"State Room"},
               11: {"items": [], "name": "Hallway 2"},
               12: {"items": [], "name": "Hallway 3"},
               13: {"items": ["invisibility spell"], "name": "Library"},
               14: {"items": ["engagement ring"], "name": "Gallery"}
               }

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

#  A dictionary linking a room to other room positions
rooms = {

    1 : {"name" : "Ballroom" ,
        "east" : 2, # Hallway
         "north" : 7, #North Vestibule
         "south" :8 }, #South Vestibule


    2 : {"name" : "Hallway",
         "north-west": 3, #Female Bathroom"
         "north-east": 4, #"Antechamber"
         "south-west": 5, #"Male Bathroom"
         "south-east": 6}, #"Throne Room"}

    3 : { "name" : "Female Bathroom" ,
          "south" : 2 } , # Hallway

    4 : { "name" : "Antechamber" ,
          "south" : 2, # Hallway
          "north" : 9},  #Blue Drawing Room

    5 : { "name" : "Male Bathroom" ,
          "north" : 2}, #Hallway

    6 : { "name" : "Throne Room" ,
          "north" : 2},

    7 : {"name" : "North Vestibule",
         "east" : 12, #Hallway 3
         "south" : 10}, # State Room

    8 : {"name": "South Vestibule",
         "east": 12, #Hallway 3
         "north" : 10}, #State Room

    9 : {"name": "Blue Drawing Room",
         "south": 11}, # Hallway 2

    10 : {"name" : "State Room",
          "north" : 7, # North Vestibule
          "east" : 12, # Hallway 3
          "south" : 8},

    11 : {"name" : "Hallway 2",
          "north" : 9, # Blue Drawing Room
          "east": 14, # Gallery
          "west": 13}, # Library

    12 : {"name" : "Hallway 3",
          "north-west" : 7, # North Vestibule
          "north-east" : 9, # Blue Drawing Room
          "west" : 10, # State Room
          "north-west" : 8, # South Vestibule
          "south-east" : 13}, # Library


    13 : {"name" : "Library",
          "east" : 11, # Hallway 2
          "west" : 12}, # Hallway 3

    14: {"name" : "Gallery",
         "west" : 11} # Hallway 2

}

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