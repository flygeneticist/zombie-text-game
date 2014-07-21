from src.player import Player
from src.world import Map
from src.scene import Scene
from src.item import Item

class Engine(object):
    def __init__(self):
        self.world_map = None
        self.start_new_game()

    def start_new_game(self):
        self.player = Player() # create the main player object
        self.load_area('./src/worlds/world000.py', 's0') # first world map
    

    def load_area(self, area_layout, start_scene):
        del self.world_map # free up memory by releasing old map/scene data
        self.world_map = Map(eval(open(area_layout).read()))
        self.serve(start_scene) # serve up the new starting position


    def serve(self, scene): 
        if scene == "death":
            print("You have died. How unfortunate. Better luck next time!")
            self.end_game()
        elif scene == "win":
            print("You made it out alive!\nYou win!!")
            self.end_game()
        elif scene == None:
            return print("You cannot move there.")
        elif scene.split('_')[0] == "map":
            data = scene.split('_')
            self.load_area('./src/worlds/world' + data[1] + '.py', data[2])
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


    def stats_check(self):
        player_stats = self.player.stats_check()
        return print("Health: {0}\nStamina: {1}".format(player_stats[0], player_stats[1]))
 