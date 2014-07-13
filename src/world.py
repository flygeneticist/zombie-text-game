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
