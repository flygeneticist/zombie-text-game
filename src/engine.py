from player import Player
from world import Map
from scene import Scene
from item import Item

class Engine(object):
    def __init__(self):
        self.world_map = None
        self.start_game()

    def start_game(self):
        print("     _______ _________ _______  _______    _______  _______      \n")
        print("    (  ____ )\__   __/(  ____ \(  ____ \  (  ___  )(  ____ \     \n")
        print("    | (    )|   ) (   | (    \/| (    \/  | (   ) || (    \/     \n")
        print("    | (____)|   | |   | (_____ | (__      | |   | || (__         \n")
        print("    |     __)   | |   (_____  )|  __)     | |   | ||  __)        \n")
        print("    | (\ (      | |         ) || (        | |   | || (           \n")
        print("    | ) \ \_____) (___/\____) || (____/\  | (___) || )           \n")
        print("    |/   \__/\_______/\_______)(_______/  (_______)|/            \n")
        print("                                                                 \n")
        print("_________          _______    ______   _______  _______  ______  \n")
        print("\__   __/|\     /|(  ____ \  (  __  \ (  ____ \(  ___  )(  __  \ \n")
        print("   ) (   | )   ( || (    \/  | (  \  )| (    \/| (   ) || (  \  )\n")
        print("   | |   | (___) || (__      | |   ) || (__    | (___) || |   ) |\n")
        print("   | |   |  ___  ||  __)     | |   | ||  __)   |  ___  || |   | |\n")
        print("   | |   | (   ) || (        | |   ) || (      | (   ) || |   ) |\n")
        print("   | |   | )   ( || (____/\  | (__/  )| (____/\| )   ( || (__/  )\n")
        print("   )_(   |/     \|(_______/  (______/ (_______/|/     \|(______/ \n")
        print("\n")
        print("~"*100)
        print("This game will challenge you to escape from a\nhospital and resuce your family! Good luck!!")
        print("~"*100 + '\n')

        # setup key objects and settings for starting the game
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
            l = self.current_scene.items
            if l == {}:
                return print("There are no items here.")
            else:
                print("The following items are in the room:")
                for k,v in l.items(): 
                    print(l[k].name)
        else:
            return print("Not a valid command")

    def take(self, item_name):
        item_name = item_name.strip().lower()
        item = self.current_scene.items[item_name]
        self.player.add_item(item)
        self.current_scene.remove_item(item_name)

    def drop(self, item_name):
        item_name = item_name.strip().lower()
        item = self.player.drop_item(item_name)
        self.current_scene.add_item(item)

    def serve(self, scene): 
        if scene == "death":
            self.end_game()
        elif scene == "win":
            self.win_game()
        elif scene == None:
            return print("You cannot move there.")
        elif scene.split('_')[0] == "map":
            self.load_area('worlds/world' + scene.split('_')[1] + '.py')
        else:
            self.current_scene = self.world_map.next_scene(scene)
            return print(self.current_scene.description)
