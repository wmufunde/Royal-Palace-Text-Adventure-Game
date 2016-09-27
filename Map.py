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
          "north" : 2}, # Hallway

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


# This is where the dictionaires go

def create_map():
    #Those dictionaries only used by initializer

    map[0] = Room()
    map[1] = Room()
    map[2] = Room()

