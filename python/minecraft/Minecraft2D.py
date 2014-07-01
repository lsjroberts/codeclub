#----------------------------
# Minecraft 2D
#----------------------------

import pygame, sys, random
from pygame.locals import *
from variables import *

fpsClock = pygame.time.Clock()

#variables for the map size
TILESIZE    = 20
MAPWIDTH    = 60
MAPHEIGHT   = 40
TOTALWIDTH  = 120
TOTALHEIGHT = 80
OFFSETLEFT  = 30
OFFSETTOP   = 20
MAPSPACING  = 10

#maps each resource to the EVENT key used to place/craft it
controls = {event:event+49 for event in range(len(resources))}

#maps each resource to the KEYBAORD key used to place/craft it
invKeys = {key:str(1+key) for key in range(len(resources))}

#the position of the player [x,y]
playerPos = [OFFSETLEFT,OFFSETTOP]

#use list comprehension to create our tilemap
tilemap = [ [DIRT for w in range(TOTALWIDTH)] for h in range(TOTALHEIGHT) ]

#add in grass to the map with about 90% coverage
for rw in range(TOTALHEIGHT):
    for cl in range(TOTALWIDTH):
        tile = DIRT
        randomNumber = random.randint(0,10)
        if randomNumber < 9:
            tile = GRASS
        tilemap[rw][cl] = tile

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE + 400, MAPHEIGHT*TILESIZE + 70))

#add a font for our inventory
INVFONT = pygame.font.Font('FreeSansBold.ttf', 12)

#choose a number of biomes to draw
numBiomes = random.randint(8, 14)
#draw these biomes
for i in range(0, numBiomes):
    #pick a random biome
    biome = random.choice(list(biomes.keys()))

    #pick a random starting point for the biome
    startPos = [
        random.randint(0,TOTALWIDTH),
        random.randint(0,TOTALHEIGHT)
    ]

    #get a randomised width and height for the biome
    width = random.randint(biomes[biome]['minSize'], biomes[biome]['maxSize'])
    height = random.randint(biomes[biome]['minSize'], biomes[biome]['maxSize'])

    #draw the biome in this range
    for x in range(startPos[0], startPos[0] + width):
        if x < len(tilemap):
            for y in range(startPos[1], startPos[1] + height):
                if y < len(tilemap[x]):
                    randomNumber = random.randint(0,100)
                    if randomNumber < biomes[biome]['coverage']:
                        tilemap[x][y] = biome

while True:

    #fill the background in black
    DISPLAYSURF.fill(BLACK)

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
        #if a key is pressed
        elif event.type == KEYDOWN:
            #if the right arrow is pressed
            if event.key == K_RIGHT and playerPos[0] < TOTALWIDTH - 1:
                #change the player's x position
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] > 0:
                #change the player's x position
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] > 0:
                #change the player's x position
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1] < TOTALHEIGHT - 1:
                #change the player's x position
                playerPos[1] += 1
            if event.key == K_SPACE:
                #what resource is the player standing on?
                currentTile = tilemap[playerPos[1]][playerPos[0]]

                #if the user doesn't already have too many...
                if inventory[currentTile] < MAXTILES:

                    #player now has 1 more of this resource
                    inventory[currentTile] += 1
                    #the player is now standing on dirt
                    tilemap[playerPos[1]][playerPos[0]] = DIRT

            for key in controls:

                #if this key was pressed
                if (event.key == controls[key]):

                    #CRAFT if shift is also pressed
                    mods = pygame.key.get_mods()
                    if mods & KMOD_SHIFT:

                        #if the item can be crafted
                        if key in craft:

                            #keeps track of whether we have the resources
                            #to craft this item
                            canBeMade = True
                            #for each item needed to craft...
                            for i in craft[key]:
                                #...if we don't have enough...
                                if craft[key][i] > inventory[i]:
                                    #...we can't craft it!
                                    canBeMade = False
                                    break
                            #if we can craft it (we have all needed resources)
                            if canBeMade == True:
                                #take each item from the inventory
                                for i in craft[key]:
                                    inventory[i] -= craft[key][i]
                                #add the crafted item to the inventory
                                inventory[key] += 1

                    #PLACE if shift wasn't pressed
                    else:

                        #get the tile the player is standing on
                        currentTile = tilemap[playerPos[1]][playerPos[0]]
                        #if we have the item to place and not too many
                        #of the item we're standing on
                        if (inventory[key] > 0 and inventory[currentTile] < MAXTILES) or (inventory[key] > 0 and currentTile == DIRT):
                            #take it from the inventory
                            inventory[key] -= 1
                            #if not full of dirt, then add it
                            if not (currentTile == DIRT and inventory[DIRT] >19):
                                #swap it with the tile we are standing on
                                inventory[currentTile] += 1
                            #place the item
                            tilemap[playerPos[1]][playerPos[0]] = key

    #offset the map within the limits of the map spacing
    if playerPos[0] > (OFFSETLEFT + MAPWIDTH - MAPSPACING) and TOTALWIDTH > (OFFSETLEFT + MAPWIDTH):
        OFFSETLEFT += 1
    if playerPos[0] < (OFFSETLEFT + MAPSPACING) and OFFSETLEFT > 0:
        OFFSETLEFT -= 1
    if playerPos[1] > (OFFSETTOP + MAPHEIGHT - MAPSPACING) and TOTALHEIGHT > (OFFSETTOP + MAPHEIGHT):
        OFFSETTOP += 1
    if playerPos[1] < (OFFSETTOP + MAPSPACING) and OFFSETTOP > 0:
        OFFSETTOP -= 1

    #loop through each row
    for row in range(OFFSETTOP, OFFSETTOP + MAPHEIGHT):
        #loop through each column in the row
        for column in range(OFFSETLEFT, OFFSETLEFT + MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct image
            DISPLAYSURF.blit(textures[tilemap[row][column]], ((column-OFFSETLEFT)*TILESIZE,(row-OFFSETTOP)*TILESIZE))

    #display the player at the correct position
    DISPLAYSURF.blit(PLAYER,((playerPos[0]-OFFSETLEFT)*TILESIZE,(playerPos[1]-OFFSETTOP)*TILESIZE))

    #draw a rectangle behind the instructions
    pygame.draw.rect(DISPLAYSURF, BLACK, (MAPWIDTH*TILESIZE,0,200,MAPHEIGHT*TILESIZE))

    #display the inventory, starting 10 pixels in
    xPosition = 10

    for item in resources:
        #add the image
        DISPLAYSURF.blit(textures[item],(xPosition,MAPHEIGHT*TILESIZE+20))
        xPosition += 30
        #add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(xPosition,MAPHEIGHT*TILESIZE+20))

        #display the key
        textObj = INVFONT.render("Key : " + invKeys[item], True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(xPosition-TILESIZE,MAPHEIGHT*TILESIZE+20+TILESIZE))

        #move along to place the next inventory item
        xPosition += 50

    #add the text showing each line of the instructions
    pos = 10
    for item in instructions:
        craftText = INVFONT.render(item, True, WHITE, BLACK)
        DISPLAYSURF.blit(craftText,(MAPWIDTH*TILESIZE+20,pos))
        pos+=20

    #update the display
    pygame.display.update()
    #create a short delay
    fpsClock.tick(24)
