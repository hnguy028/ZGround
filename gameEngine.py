"""
    gameEngine.py
"""
from Window import *
from player import *
import pygame


class GameEngine:

    def __init__(self):
        self.state = State.START_MENU

        self.surface_loaded = False
        self.window = None

        self.mm_music = None
        self.game_music = None

        self.player = None

        # testing player variables
        self.p_move_speed = 10

    def handle_event(self, event):
        if self.state == State.START_MENU:
            if event.type == pygame.KEYDOWN:
                self.mm_music.stop()
                self.state = State.GAME
                self.load_game()

                self.player.set_location(10, 10)

        elif self.state == State.GAME:
            if event.type == pygame.KEYDOWN:
                self.player.handle_key_down(event)
            elif event.type == pygame.KEYUP:
                self.player.handle_key_up(event)
        else:
            pass

    def load_window(self):
        if not self.surface_loaded:
            self.surface_loaded = True
            self.window = WindowSurface(HUDSIZE_TOP + HUDSIZE_BOTTOM, ROOMWIDTH, ROOMHEIGHT)

            self.mm_music = pygame.mixer.Sound(AUDIO_DIRECTORY + "teamwork.wav")
            self.mm_music.play(-1)

            self.player = Player(STICKMAN_DIRECTORY + CHAR_SPRITE_SHEET_FILENAME, HW, HH)

    def load_game(self):
        self.game_music = pygame.mixer.Sound(AUDIO_DIRECTORY + "aspire.wav")
        self.game_music.play(-1)

    def start(self):
        pass

    def stop(self):
        pass

    def draw_game(self):
        self.window.surface.fill((86, 244, 66, 0))

        # pygame.draw.rect(screen, color, (x,y,width,height), thickness)
        pygame.draw.rect(self.window.surface, (0, 0, 0, 0),
                         (0, FRAMEPIXELHEIGHT - 10, FRAMEPIXELWIDTH, 10))

        self.player.move()
        self.player.draw_idle(self.window.surface)

    def draw_start_menu(self):
        self.window.surface.fill((66, 133, 244, 0))
        self.player.draw_idle(self.window.surface)


class State:
    INITIAL_LOAD, START_MENU, GAME = range(3)
