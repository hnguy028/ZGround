"""
    player.py
"""
from spriteSheet import *
from constants import *

class Player:

    def __init__(self, image_file, x, y):
        self.image_file = image_file
        self.x = x
        self.y = y

        self.sprite_sheet = SpriteSheet(self.image_file, 10, 10)
        self.central_handle = 4
        self.draw_index = 0

    def move(self):
        pass

    def draw(self, surface):
        self.sprite_sheet.draw(surface, self.draw_index % self.sprite_sheet.total_cell_count,
                               self.x, self.y, self.central_handle)
        self.draw_index += 1

    def draw_idle(self, surface):
        min_i = 0
        self.sprite_sheet.draw(surface, min_i + (self.draw_index % 2),
                               self.x, self.y, self.central_handle)
        self.draw_index += 1