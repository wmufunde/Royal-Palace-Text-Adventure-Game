from Room import Room
from Enemy import *

reusable_items = ["sword", "crossbow", "pack of matches", "shield"]

ballroom = Room("Ballroom", ["sword"], [])
hallway = Room("Hallway", ["crossbow"], [])
female_bathroom = Room("Female Bathroom", ["pack of matches"], [])
antechamber = Room("Antechamber", [], [dark_elf])
male_bathroom = Room("Male Bathroom", ["shield"], [])
throne_room = Room("Throne Room", [], [goblin])
north_vestibule = Room("North Vestibule", ["super speed spell"], [harpy])
south_vestibule = Room("South Vestibule", ["lightning spell"], [])
blue_drawing_room = Room("Blue Drawing Room", ["freezing spell"], [malignant_spirit])
state_room = Room("State Room", [], [])
hallway_2 = Room("Hallway 2", [], [goblin])
hallway_3 = Room("Hallway 3", [], [])
library = Room("Library", ["invisibility spell"], [malignant_spirit])
gallery = Room("Gallery", [], [malignant_spirit])

#  A dictionary linking a room to other room positions
rooms = {

    ballroom: {"east": hallway,
                "north": north_vestibule,
                "south": south_vestibule},

    hallway : {"north-west": female_bathroom,
               "north-east": antechamber,
               "south-west": male_bathroom,
               "south-east": throne_room},

    female_bathroom : { "name" : female_bathroom,
                        "south" : hallway},

    antechamber : {"south" : hallway,
                   "north" : blue_drawing_room},

    male_bathroom : {"north" : hallway},

    throne_room : {"north" : hallway},

    north_vestibule : {"east" : hallway_3,
                       "south": state_room},

    south_vestibule : {"east": hallway_3,
                       "north" : state_room},

    blue_drawing_room : {"south": hallway_2},

    state_room : {"north" : north_vestibule,
                  "east" : hallway_3,
                  "south" : south_vestibule},

    hallway_2 : {"north" : blue_drawing_room,
                 "east": gallery,
                 "west": library},

    hallway_3 : {"north-west" : north_vestibule,
                 "north-east" : blue_drawing_room,
                 "west" : state_room,
                 "north-west" : south_vestibule,
                 "south-east" : library},

    library : {"east" : hallway_2,
               "west" : hallway_3},

    gallery : {"west" : hallway_2}
}

current_room = ballroom
current_room = rooms[current_room]["east"]
current_room = rooms[current_room]["south-west"]

print(current_room.name)