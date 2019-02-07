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

        self.gravity = 5
        self.vertical_velocity = -5
        self.walk_speed = 5

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def move(self):
        self.y -= self.vertical_velocity

        if self.move_up:
            self.y -= 10

        if self.move_down:
            self.y += self.walk_speed

        self.y = min(FRAMEPIXELHEIGHT - 10 - self.sprite_sheet.cell_height / 4, self.y)

        if self.move_left:
            self.x -= self.walk_speed

        if self.move_right:
            self.x += self.walk_speed

    def handle_key_down(self, e):
        # if shift key is pressed init player running
        # if e.key in (K_LSHIFT, K_RSHIFT):
        #     self.running = True

        if e.key == pygame.K_UP:
            self.move_up = True
            self.move_down = False
        elif e.key == pygame.K_DOWN:
            self.move_down = True
            self.move_up = False
        elif e.key == pygame.K_LEFT:
            self.move_left = True
            self.move_right = False
        elif e.key == pygame.K_RIGHT:
            self.move_right = True
            self.move_left = False
        # elif e.key == C_ATTACK:
        #     if not self.attackConductor:
        #         self.attack(None)
        #     else:
        #         self.stop_attack()
        # elif e.key == K_KP1:
        #     self.take_damage(5)

    def handle_key_up(self, e):
        if e.key == pygame.K_UP:
            self.move_up = False
        elif e.key == pygame.K_DOWN:
            self.move_down = False
        elif e.key == pygame.K_LEFT:
            self.move_left = False
        elif e.key == pygame.K_RIGHT:
            self.move_right = False

    def set_location(self, _x, _y):
        self.x = _x
        self.y = _y

    def draw(self, surface):
        self.sprite_sheet.draw(surface, self.draw_index % self.sprite_sheet.total_cell_count,
                               self.x, self.y, self.central_handle)
        self.draw_index += 1

    def draw_test(self, surface):
        min_i = 56
        self.sprite_sheet.draw(surface, min_i + (self.draw_index % 4),
                               self.x, self.y, self.central_handle)
        self.draw_index += 1

    def draw_jump(self, surface):
        min_i = 56
        self.sprite_sheet.draw(surface, min_i + (self.draw_index % 4),
                               self.x, self.y, self.central_handle)
        self.draw_index += 1

    def draw_idle(self, surface):
        min_i = 62
        self.sprite_sheet.draw(surface, min_i + (self.draw_index % 2),
                               self.x, self.y, self.central_handle)
        self.draw_index += 1

    def draw_run(self, surface, forward=True):
        min_i = 1
        self.sprite_sheet.draw(surface, min_i + (self.draw_index % 2),
                               self.x, self.y, self.central_handle)
        self.draw_index += 1