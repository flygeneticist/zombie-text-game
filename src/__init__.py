from engine import Engine

# create the game engine to start the game
e = Engine()

# quick lookup dict for all valid player input actions linked back to the engine function
valid_actions = {"look":e.look,"move":e.move,"take":e.take,"drop":e.drop}

while (True):
    # get player's action input
    action = input("> ").strip().lower().split(" ")

    # check that the action has two words (verb and object)
    if (action[0] in valid_actions) and (len(action) == 2):
        valid_actions[action[0]](action[1])
    elif (action[0] == 'help'):
        print('The following are valid commands:\n',
                'look <north, south, east, west>\n',
                'move <north, south, east, west>\n',
                'take <item name>\n',
                'drop <item name>\n'
            )
    else:
        print("Not a valid action!")
