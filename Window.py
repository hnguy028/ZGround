from constants import *
import pygame


# Window surface definition
class WindowSurface:

    def __init__(self, hud_size, room_width, room_height):
        self.surfaceWidth = TILESIZE * room_width
        self.surfaceHeight = TILESIZE * room_height + TILESIZE * hud_size

        # create window
        self.surface = pygame.display.set_mode((self.surfaceWidth, self.surfaceHeight), 0, TILESIZE)
        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(pygame.image.load(GAME_ICON))
