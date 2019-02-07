"""
    world.py
"""
from constants import *


class World:
    def __init__(self):
        self.floor = FRAMEPIXELHEIGHT - 10

    # return list of objects collidable with character
    def get_collision_objects(self):
        pass

    # given player coordinates, get floor / platform coords below character
    def get_below(self, p_x, p_y):
        pass

    # get y coordinate of floor
    def get_floor(self):
        return self.floor
