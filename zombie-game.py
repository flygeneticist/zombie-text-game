from src.engine import Engine
import pickle


def game_intro():
    print("\n")
    print("     _______ _________ _______  _______    _______  _______      \n")
    print("    (  ____ )\__   __/(  ____ \(  ____ \  (  ___  )(  ____ \     \n")
    print("    | (    )|   ) (   | (    \/| (    \/  | (   ) || (    \/     \n")
    print("    | (____)|   | |   | (_____ | (__      | |   | || (__         \n")
    print("    |     __)   | |   (_____  )|  __)     | |   | ||  __)        \n")
    print("    | (\ (      | |         ) || (        | |   | || (           \n")
    print("    | ) \ \_____) (___/\____) || (____/\  | (___) || )           \n")
    print("    |/   \__/\_______/\_______)(_______/  (_______)|/            \n")
    print("\n")
    print("\n")
    print("_________          _______    ______   _______  _______  ______  \n")
    print("\__   __/|\     /|(  ____ \  (  __  \ (  ____ \(  ___  )(  __  \ \n")
    print("   ) (   | )   ( || (    \/  | (  \  )| (    \/| (   ) || (  \  )\n")
    print("   | |   | (___) || (__      | |   ) || (__    | (___) || |   ) |\n")
    print("   | |   |  ___  ||  __)     | |   | ||  __)   |  ___  || |   | |\n")
    print("   | |   | (   ) || (        | |   ) || (      | (   ) || |   ) |\n")
    print("   | |   | )   ( || (____/\  | (__/  )| (____/\| )   ( || (__/  )\n")
    print("   )_(   |/     \|(_______/  (______/ (_______/|/     \|(______/ \n")
    print("\n")
    print("\n")
    print("~"*100)
    print("This game will challenge you to escape from a\nhospital and resuce your family! Good luck!!")
    print("~"*100 + '\n')
    

def pick_loader():    
    # get player input and load the correct game start
    print("Please from choose from one of the following options:\n1) Start a new game\n2) Load a saved game")
    try:
        pick = int(input("Enter your choice: ").strip())
    except:
        print("That is not a valid choice. Please try again.\n")
        pick_loader()
    else:
        if pick == 1:
            return start_new_game()
        elif pick == 2:
            name = input("Enter your character's name: ").strip()
            return load_saved_game(name)
        else:
            print("That is not a valid choice. Please try again.\n")
            pick_loader()


def start_new_game():
    return Engine()


def load_saved_game(name): 
    '''Loads pickled game engine from the saves folder. Load the last map and scene.'''
    with open(r"./saves/"+name+".pickle", "rb") as input_file:
        return pickle.load(input_file)


def save_game():
    '''Copies all game data files in TEMP folder into a saved game folder, based on player\'s name'''
    save = input("Are you sure you want to proceed?\nThis will overwrite any previously saved game data? y/n: ").strip().lower()
    if save == 'y':
        with open(r"./saves/" + e.player.name + ".pickle", "wb") as output_file:
            pickle.dump(e, output_file)
        print("Your game has been saved!")
    elif save == 'n':
        pass
    else:
        print("Not a valid option. Please try again.")
        save_game()


def exit_game():
    quit = input("Are you sure you want to exit the game? y/n: ").strip().lower()
    if quit == 'y':
        print("Thanks for playing!")
        end_game()
    elif quit == 'n':
        pass
    else:
        print("Not a valid option. Please try again.")
        exit_game()


def end_game():
    exit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run-time commands to handle passing player input back into the game engine.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
game_intro()
e = pick_loader()

# quick lookup dict for all valid player input actions linked back to the engine function
valid_actions = {   "look":e.look,"move":e.move,"take":e.take,"drop":e.drop, 
                    "find":e.find, "check":e.check_inv, "examine":e.examine,
                    "save":save_game, "exit":exit_game
                }

while (True):
    # get player's action input
    action = input("> ").strip().lower().split(" ")

    # check that the action has two words (verb and object)
    if (action[0] in valid_actions) and (len(action) == 2):
        valid_actions[action[0]](action[1])
    # chekc if action is save or exit commands in don't use an arg
    elif (action[0] == 'save') or (action[0] == 'exit'):
        valid_actions[action[0]]()
    elif (action[0] == 'help'):
        print('The following are valid commands:\n',
                'look <north, south, east, west> => Examines a given direction.\n',
                'move <north, south, east, west> => Moves your character in a given direction.\n',
                'find <items, npc>               => Finds all items or NPCs in your current location.\n',
                'examine <item name>             => Find out more about an item(description, weight, attack damage).\n',
                'take <item name>                => Picks up a item and put it in your inventory.\n',
                'drop <item name>                => Drops an item from your inventory.\n',
                'check inv                       => Gets a list of all items currently in your inventory.\n',
                'save                            => Saves your current game state.\n',
                'exit                            => Exits the game.\n'
            )
    else:
        print("Not a valid action!")
