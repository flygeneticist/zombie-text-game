class Engine(object):
    def __init__(self):
        self.world_map = None
        self.start_game()

    def start_game(self):
        self.player = Player(input("Enter your character's name: "))
        self.load_area('./worlds/world000.py') # starting world/area
        print(" _______ _________ _______  _______    _______  _______          \n")
        print("(  ____ )\__   __/(  ____ \(  ____ \  (  ___  )(  ____ \         \n")
        print("| (    )|   ) (   | (    \/| (    \/  | (   ) || (    \/         \n")
        print("| (____)|   | |   | (_____ | (__      | |   | || (__             \n")
        print("|     __)   | |   (_____  )|  __)     | |   | ||  __)            \n")
        print("| (\ (      | |         ) || (        | |   | || (               \n")
        print("| ) \ \_____) (___/\____) || (____/\  | (___) || )               \n")
        print("|/   \__/\_______/\_______)(_______/  (_______)|/                \n")
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
        self.serve('s0') # start the game in your hospital room on 3rd floor(s0)
        
    def end_game(self):
        print("You have died. How unfortunate. Better luck next time!")
        exit()

    def win_game(self):
        print("You made it to the stairwell and...presuambly made it out alive.\nYou win!!")
        exit()

    def load_area(self, area_layout):
        # world_layout should refer to a file in which the area's data is stored
        del self.world_map
        self.world_map = Map(eval(open(area_layout).read()))

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
            self.player.visited_scenes.append(self.current_scene.name)
            return print("You enter a " + self.current_scene.description)


class Map(object):
    def __init__(self, world_layout):
        self.world = world_layout

    def next_scene(self, scene_name):
        try:
            next = self.world[scene_name]
        except ValueError:
            return print("That scene does not exist!")
        else:
            return next


class Scene(object):
    def __init__(self, name, description, layout, items, npc):
        self.name = name
        self.description = description
        self.layout = layout # directions and which scene they lead to.
        self.items = items
        self.npc = npc

class Player(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.maxhealth = 100
        self.stamina = 100
        self.maxstamina = 100
        self.curr_scene = None
        self.visited_scenes = []

    def look(self, direction):
        try:
            imagery = e.current_scene.layout[direction]['look']
        except KeyError:
            imagery = "That is not a valid direction!"
        else:
            if imagery == None: 
                imagery = "There is nothing to see in that direction."
        return print(imagery)

    def move(self, direction):
        try:
            destination = e.current_scene.layout[direction]['move']
        except: 
            destination = None
        return e.serve(destination)

    def take(self, item):
        return print("You picked up a {}".format(e.current_scene.items[item]))

    def drop(self, item):
        return print("You dropped up a {}".format(e.current_scene.items[item]))




# create the game engine to start the game
e = Engine() 
# quick lookup dict for all valid player input actions linked back to the engine function
valid_actions = {"look":e.player.look,"move":e.player.move,"take":e.player.take,"drop":e.player.drop}

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
