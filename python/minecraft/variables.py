import pygame

#--------------------------
# Minecraft 2D -- Variables
#--------------------------


#the maximum number of each resource that can be held
#----------------------------------------------------

MAXTILES  = 255


#the title bar text/image
#------------------------

pygame.display.set_caption('pygame window')
pygame.display.set_icon(pygame.image.load('player.png'))


#variables for representing colours
#----------------------------------

BLACK = (0,     0,     0  )
BROWN = (153,   76,    0  )
GREEN = (0,     255,   0  )
BLUE  = (0,     0,     255)
WHITE = (255,   255,   255)


#variables representing the different resources
#----------------------------------------------

DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
SAND    = 4
TREE    = 5


#a list of all game resources
#----------------------------

resources = [DIRT,GRASS,WATER,BRICK,SAND]
biomes    = {
    WATER: {
        'minSize': 5,
        'maxSize': 20,
        'coverage': 80
    },
    SAND: {
        'minSize': 10,
        'maxSize': 60,
        'coverage': 80
    },
    TREE: {
        'minSize': 10,
        'maxSize': 80,
        'coverage': 30
    }
}


#a dictionary linking resources to textures
#------------------------------------------

textures =   {
                DIRT    : pygame.image.load('dirt.png'),
                GRASS   : pygame.image.load('grass.png'),
                WATER   : pygame.image.load('water.png'),
                BRICK   : pygame.image.load('brick.png'),
                SAND    : pygame.image.load('sand.png'),
                TREE    : pygame.image.load('tree.png')
             }


#the number of each resource that we have to start with
#------------------------------------------------------

inventory =   {
                DIRT    : 10,
                GRASS   : 10,
                WATER   : 10,
                BRICK   : 0,
                SAND    : 0,
                TREE    : 0
            }


#the player image
#----------------

PLAYER = pygame.image.load('player.png')


#rules to make new objects
#-------------------------

craft = {
            BRICK    : { WATER : 1, DIRT : 2 }
        }


#instructions list
#-----------------

instructions =  [
                    "Minecraft 2D",
                    "Instructions:",
                    "   ARROW KEYS = move",
                    "   SPACE = Pick up tile",
                    "   NUMBER KEYS = Place tile",
                    "   SHIFT + NUMBER KEYS = Craft tile",
                    "",
                    "Crafting Rules:",
                    "   BRICK = 2xDIRT + 1xWATER"
                ]
