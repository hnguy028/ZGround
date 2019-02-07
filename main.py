from constants import *
import pygame
from gameEngine import *
from player import *
from spriteSheet import *
import sys

# global variables
mainClock = pygame.time.Clock()
running = True

pygame.init()

if __name__ == "__main__":

    engine = GameEngine()
    engine.load_window()

    while running:
        if engine.state == State.GAME:
            for event in pygame.event.get():
                # handle exit button press
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    engine.handle_event(event)

            engine.draw_game()

        elif engine.state == State.START_MENU:
            for event in pygame.event.get():
                # handle exit button press
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    engine.handle_event(event)
            engine.draw_start_menu()

        else:
            print("State Error")
            pygame.quit()
            sys.exit()

        pygame.display.update()
        mainClock.tick(30)

    pygame.quit()
    sys.exit()
