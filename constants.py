# Global constants and variable definitions

GAME_TITLE = "Sandbox Game"
GAME_ICON = 'resources/menu/icon.png'

RESOURCE_DIRECTORY = 'resources/'
UI_DIRECTORY = RESOURCE_DIRECTORY + 'menu/'

STICKMAN_DIRECTORY = RESOURCE_DIRECTORY + 'test/'
CHARACTER_DIRECTORY = RESOURCE_DIRECTORY + 'characters/'
COLLECTIBLES_DIRECTORY = RESOURCE_DIRECTORY + 'items/'
ATTACKS_DIRECTORY = RESOURCE_DIRECTORY + 'attacks/'
MAPS_DIRECTORY = RESOURCE_DIRECTORY + 'maps/'
FONT_DIRECTORY = RESOURCE_DIRECTORY + 'fonts/'
AUDIO_DIRECTORY = RESOURCE_DIRECTORY + 'audio/'
SAVE_DIRECTORY = RESOURCE_DIRECTORY + 'saves/'

MAIN_MENU_DIRECTORY = UI_DIRECTORY + 'mainmenu/'
UI_COMPONENTS_DIRECTORY = UI_DIRECTORY + 'components/'
UI_CURSOR_DIRECTORY = UI_DIRECTORY + 'cursor/'


########## Game Information
FPS = 30

########## Character Information
CHARACTER_NAME = "tester"
CHAR_WALKRATE = 10
CHAR_RUNRATE = 20

######### Inventory Defaults
INITIAL_INVENTORY_SIZE = 13
DEFAULT_INV_GRID_WIDTH = 5
DEFAULT_INV_GRID_HEIGHT = 3

# Character orientation variables
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

CHARACTER_WIDTH = 0
CHARACTER_HEIGHT = 0

# TMX object codes
COLLECTABLE_CODE = 'collectables'

# Window variables
# Tile size in pixels
TILESIZE = 32


# Size of the hud in (32 x 32) tiles
HUDSIZE_TOP = 1
HUDSIZE_BOTTOM = 4

# Size of the window frame in (32 x 32) tiles
FRAMEWIDTH = 15
FRAMEHEIGHT = 15 + HUDSIZE_TOP + HUDSIZE_BOTTOM

FRAMEPIXELWIDTH = FRAMEWIDTH * TILESIZE
FRAMEPIXELHEIGHT = FRAMEHEIGHT * TILESIZE

# Size of the room frame in (32 x 32) tiles
ROOMWIDTH = 15
ROOMHEIGHT = 15

MAX_ALPHA = 255
MIN_ALPHA = 0