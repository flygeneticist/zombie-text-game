from player import Player
from world import Map
from scene import Scene
from item import Item

class Engine(object):
    def __init__(self):
        self.world_map = None
        self.game_intro()
        self.pick_loader()

    def game_intro(self):
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
        

    def pick_loader(self):    
        # get player input and load the correct game start
        print("Please from choose from one of the following options:\n1) Start a new game\n2) Load a saved game")
        pick = int(input("Enter your choice: ").strip())
        if pick == 1:
            self.start_new_game()
        elif pick == 2:
            name = input("Enter your character's name: ").strip()
            self.load_saved_game(name)
            print("Sorry! Loading / saving games are not available now!")
            exit()
        else:
            print("That is not a valid choise. Please try again.\n")
            self.pick_loader()


    def load_saved_game(self, name): 
        '''Copies saved game data to the TEMP folder based on the character name used at it's creation 
        from a save folder of the same name'''
        pass

    def start_new_game(self):
        self.player = Player() # create the main player object
        self.load_area('./worlds/world000.py') # first world map
        

    def end_game(self):
        print("You have died. How unfortunate. Better luck next time!")
        exit()


    def win_game(self):
        print("You made it out alive!\nYou win!!")
        exit()


    def load_area(self, area_layout):
        del self.world_map # free up memory by releasing old map/scene data
        self.world_map = Map(eval(open(area_layout).read()))
        self.serve('s0') # serve up the new starting position


    def serve(self, scene, scene2=""): 
        if scene == "death":
            self.end_game()
        elif scene == "win":
            self.win_game()
        elif scene == None:
            return print("You cannot move there.")
        elif scene.split('_')[0] == "map":
            self.load_area('worlds/world' + scene.split('_')[1] + '.py')
            self.current_scene = self.world_map.next_scene(scene2)
            return print(self.current_scene.description)
        else:
            self.current_scene = self.world_map.next_scene(scene)
            return print(self.current_scene.description)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Player command functions will serve as the interface for the player and the rest of the game.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def look(self, direction):
        try:
            imagery = self.current_scene.layout[direction]['look']
        except KeyError:
            imagery = "That is not a valid direction."
        else:
            if imagery == None: 
                imagery = "There is nothing to see in that direction."
        return print(imagery)


    def move(self, direction):
        try:
            destination = self.current_scene.layout[direction]['move']
        except KeyError: 
            destination = None
        return self.serve(destination)


    def find(self, command):
        if command == "items":
            self.current_scene.list_items()
        elif command == "npc":
            return print("No NPCs found.")
        else:
            return print("Not a valid command.")


    def check_inv(self, command="inv"):
        return self.player.check_inv()


    def take(self, command):
        item_name = command.strip().lower()
        try:
            item = self.current_scene.items[item_name]
        except KeyError:
            return print("{} is not an item that can be taken.".format(item_name))
        else:
            self.player.add_item(item)
            self.current_scene.remove_item(item_name)


    def drop(self, command):
        item_name = command.strip().lower()
        try:
            item = self.player.inventory[item_name][0]
        except KeyError:
            return print("{} is not an item in your inventory.".format(item_name))
        else:
            item = self.player.drop_item(item)
            self.current_scene.add_item(item)


    def examine(self, command):
        return self.current_scene.examine_item(command)


    def save_game(self, name=self.player.name):
        '''Copies all game data files in TEMP folder into a saved game folder.'''
        save = input("Are you sure you want to overwrite the previously saved game? y/n: ").strip().lower()
        if save == 'y':
            # do some file shuffling here.....
            print("Your game has been saved!")
        elif save == 'n':
            pass
        else:
            print("Not a valid option. Please try again.")
            self.save_game()


    def exit_game(self):
        quit = input("Are you sure you want to exit the game? y/n: ").strip().lower()
        if quit == 'y':
            print("Thanks for playing!")
            exit()
        elif quit == 'n':
            pass
        else:
            print("Not a valid option. Please try again.")
            self.exit_game()