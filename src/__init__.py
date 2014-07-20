from engine import Engine

# create the game engine to start the game
e = Engine()

# quick lookup dict for all valid player input actions linked back to the engine function
valid_actions = {   "look":e.look,"move":e.move,"take":e.take,"drop":e.drop, 
                    "find":e.find, "check":e.check_inv, "examine":e.examine,
                    "save":e.save_game, "exit":e.exit_game
                }

while (True):
    # get player's action input
    action = input("> ").strip().lower().split(" ")

    # check that the action has two words (verb and object)
    if (action[0] in valid_actions) and (len(action) == 2):
        valid_actions[action[0]](action[1])
    elif (action[0] == 'help'):
        print('The following are valid commands:\n',
                'look <north, south, east, west> => Examines a given direction.\n',
                'move <north, south, east, west> => Moves your character in a given direction.\n',
                'find <items, npc>               => Finds all items or NPCs in your current location.\n',
                'examine <item name>             => Find out more about an item(description, weight, attack damage).\n',
                'take <item name>                => Picks up a item and put it in your inventory.\n',
                'drop <item name>                => Drops an item from your inventory.\n',
                'check inv                       => Gets a list of all items currently in your inventory.\n',
                'save <name(optional)>           => Saves your current game state for later.\n',
                'exit                            => Exits the game.\n'
            )
    else:
        print("Not a valid action!")
