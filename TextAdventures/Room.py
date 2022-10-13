class Wall:
    def __init__(self, color, description):
        self.color = color
        self.description= description

class Door:
    pass

class Window:
    pass

class Room:
    def __init__(self, description,name, **kwargs):
        self.description = description
        self.name = name
    
    def get_room_description(self):
        return self.description
    def set_room_description(self, d):
        self.description = d
    def add_scene_left(self):
        pass
    def add_scene_right(self):
        pass
    def add_scene_forward(self):
        pass
    def add_scene_backward(self):
        pass
    def add_scene_up(self):
        pass
    def add_scene_down(self):
        pass
    def add_neighbour_north(self):
        pass
    def add_neighbour_south(self):
        pass
    def add_neighbour_east(self):
        pass
    def add_neighbour_west(self):
        pass
    def run():
        pass
    
    
