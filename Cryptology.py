import pygame
from pygame import mixer
pygame.init()
from classes import Backdrop
from classes import Menu
from classes import Toggle
from classes import Object
import time

##### Colours #####
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
PINK  = (255, 192, 203)

##### Screen Initialisation #####
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 640
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
favicon = pygame.image.load("images\\skull_room1.png")
pygame.display.set_caption("CRYPTOLOGY")
pygame.display.set_icon(favicon)

##### Other Variables #####
# Game
done = False       
coffinOpen = False
skullPlaced = False
chestOpen = False
gemPlaced = False

# Time
clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks()
timet = 180 #time in seconds
times = pygame.USEREVENT+1
pygame.time.set_timer(times, 1000)

# Font 
font = pygame.font.SysFont(("Lucida Console"), 28)

# Room
global room
room = 0

# Inv
placeholder = pygame.image.load("images\\flavourtextbar.png")
inventoryinfo = [] # list of GAME NAME FILE ITEMS IN INVENTORY
inventory = [] # list of REAL OBJECT  NAME OF ITEMS
# first inv is [24, 576]
# second inv is [120, 576]
# a + (n-1)d
# 24 + (n-1)96
# 24 + 96n - 96
# 96n -72

# Music
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
chestopen = pygame.mixer.Sound("audio\\chestopen.wav")
mixer.init()
mixer.music.load('audio\\academymusic.wav')
mixer.music.play()

##### Main Program Loop #####
while not done:
    keys = pygame.key.get_pressed()
    ##### Events Loop #####
    if room <= 0.8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    ##### Game logic #####

    ##### Drawing code #####
# ROOM 0.5 = Instructions
# ROOM 1 = COFFIN ROOM 
# ROOM 2 = SPAWN ROOM 
# ROOM 3 = LIBRARY/ARCHIVES
# ROOM 4 =  BASEMENT
    #def timeUpdate():
        #global min
        #countdown  = font.render(f"{gameTime}{min}", True, WHITE)
        #screen.blit(countdown, (1040, 550))    

        class DrawUI():
            def drawleft(self, screen):
                global arrowleft
                arrowleft = Toggle()
                arrowleft.toggleImage = pygame.image.load("images\\arrowleft.png")
                arrowleft.x = 0
                arrowleft.y = 240
                arrowleft.draw(screen)

            def drawright(self, screen):
                global arrowright
                arrowright = Toggle()
                arrowright.toggleImage = pygame.image.load("images\\arrowright.png")
                arrowright.x = 1152
                arrowright.y = 240
                arrowright.draw(screen)     

        if room == 0:
            # DRAW BACKDROP (BLURRED START SCREEN)
            backdrop = Backdrop()
            backdrop.draw(screen)

            # DRAW TITLE
            title = Menu()
            title.draw(screen)

            # DRAW INFO BUTTON
            info = Toggle()
            info.toggleImage = pygame.image.load("images\\info.png")
            info.x = 500
            info.y = 400

            info.draw(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if info.rect.collidepoint(pygame.mouse.get_pos()): # is some button clicked
                    time.sleep(0.25)
                    room = 0.5 # Tutorial room
    
            # DRAW START BUTTON
            start = Toggle()
            start.draw(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.rect.collidepoint(pygame.mouse.get_pos()): # is some button clicked
                    time.sleep(0.25)
                    room = 0.75 # Spawn room which happens to be room 2

        if room == 0.5:
            instructions = Backdrop()
            instructions.roomImage = pygame.image.load("images\\instructions.png")
            instructions.draw(screen)
            if keys[pygame.K_SPACE]:
                room = 0

        if room == 0.75:
            loading = Backdrop()
            loading.roomImage = pygame.image.load("images\\loading.png")
            loading.draw(screen)
            if keys[pygame.K_SPACE]:
                time.sleep(0.25)
                room = 2
            if keys[pygame.K_a]:
                time.sleep(0.25)
                room = 0.8
        if room == 0.8:
            lore = Backdrop()
            lore.roomImage = pygame.image.load("images\\lore.png")
            lore.draw(screen)
            if keys[pygame.K_SPACE]:
                time.sleep(0.25)
                room = 2
        
# Done: REMINDER: INDENT THIS WITH IF ROOM >= 1 TO SHOW THE INVENTORY BAR IN ALL ROOMS 
    elif 1 <= room <= 8:   #if game started
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == times:
                timet -= 1
            
        if timet <= 0:
            room = 7
        #draw taskbar
        taskbar = Menu()
        taskbar.menuImage = pygame.image.load("images\\taskbar.png")
        taskbar.x = 0
        taskbar.y = 480
        taskbar.draw(screen)

        if room == 1:
            # DRAW BACKGROUND
            room1 = Backdrop()
            room1.roomImage = pygame.image.load("images\\room1.png")
            room1.draw(screen)

            # DRAW INTERACTIVES
            closedcoffin_room1 = Object()
            closedcoffin_room1.x = 48
            closedcoffin_room1.y = 384
            # DRAW SKULL
            skull_room1 = Object()
            skull_room1.objectImage = pygame.image.load("images\\skull_room1.png")
            skull_room1.objectPurpose = "SKULL"
            skull_room1.objectName = "skull_room1"
            skull_room1.x = 360
            skull_room1.y = 268

            if coffinOpen == False:
                closedcoffin_room1.objectImage = pygame.image.load("images\\closedcoffin_room1.png")
                closedcoffin_room1.draw(screen)
            else:
                closedcoffin_room1.objectImage = pygame.image.load("images\\opencoffin_room1.png")
                closedcoffin_room1.draw(screen)   
                if skullPlaced == False and "SKULL" not in inventory:
                    skull_room1.draw(screen)  

            # DRAW FLAVOUR TEXT FOR ROOM
            if room1.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(placeholder, [0,480])
                rendertext = font.render("*You are in a dark room, filled with coffins.", 'BLACK', True)
                screen.blit(rendertext, [12,500])
            

            # DRAW ARROWS AND CHECK IF THEY'RE BEING CLICKED
            UI = DrawUI()
            UI.drawright(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrowright.rect.collidepoint(pygame.mouse.get_pos()):
                    room = 2
                    time.sleep(0.5)
                
                #coffin
                if "KEY" in inventory:
                    if closedcoffin_room1.rect.collidepoint(pygame.mouse.get_pos()):
                        coffinOpen = True
                        room = 1.5
                        
                if closedcoffin_room1.rect.collidepoint(pygame.mouse.get_pos()) and coffinOpen == True:
                    room = 1.5

                if closedcoffin_room1.rect.collidepoint(pygame.mouse.get_pos()) and "KEY" not in inventory:
                    screen.blit(placeholder, [0,480])
                    rendertext = font.render("*It's dusty.", 'BLACK', True)
                    screen.blit(rendertext, [12,500])    

                #skull
                if skull_room1.objectCollected == False and "SKULL" not in inventory:
                    skull_room1.rect = skull_room1.objectImage.get_rect(topleft = (skull_room1.x, skull_room1.y))
                    if skull_room1.rect.collidepoint(pygame.mouse.get_pos()):
                        time.sleep(0.25)
                        screen.blit(placeholder, [0, 480])
                        skull_room1.add(inventory)
                        skull_room1.infoadd(inventoryinfo)
                        skull_room1.objectCollected = True

        elif room == 1.5: #JOURNAL SCREEN
            journal34 = Backdrop()
            journal34.roomImage = pygame.image.load("images\\journal34_room1.png")
            journal34.draw(screen)
            rendertext = font.render("*You found a journal.", 'BLACK', True)
            screen.blit(rendertext, [12,500])    

            if keys[pygame.K_SPACE]:
                if "KEY" in inventory:
                    inventory.remove(key_room4.objectPurpose)
                    inventoryinfo.remove(key_room4.objectName)
                room = 1

        elif room == 2: # DONE: REMINDER: REDO THE BACKGROUND, MAKE THE DOOR A SEPARATE OBJECT CLASS INSTANCE
            # DRAW BACKGROUND
            room2 = Backdrop()
            room2.roomImage = pygame.image.load("images\\room2.png")
            room2.draw(screen)

            # DRAW FLAVOUR TEXT FOR ROOM
            if room2.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(placeholder, [0,480])
                rendertext = font.render("*You are in a room with a locked door.", 'BLACK', True)
                screen.blit(rendertext, [12,500])

            # DRAW INTERACTIVES
            torch_room2 = Object()
            torch_room2.objectPurpose = "TORCH"
            torch_room2.objectName = "torch_room2"
            torch_room2.draw(screen)
            
            torch2_room2 = Object()
            torch2_room2.objectPurpose = "TORCH"
            torch2_room2.objectName = "torch_room2"
            if "TORCH" not in inventory:
                torch2_room2.x = 864
                torch2_room2.y = 144
                torch2_room2.draw(screen)

            door_room2 = Object()
            door_room2.objectImage = pygame.image.load("images\\door_room2.png")
            door_room2.x = 576
            door_room2.y = 48
            door_room2.draw(screen)
            if door_room2.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(placeholder, [0,480])
                rendertext = font.render("*Only a special flame could vanquish this darkness.", 'BLACK', True)
                screen.blit(rendertext, [12,500])
                

            # DRAW ARROWS AND CHECK IF THEY'RE BEING CLICKED
            UI = DrawUI()
            UI.drawleft(screen)
            UI.drawright(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if navigating room
                if arrowleft.rect.collidepoint(pygame.mouse.get_pos()):
                    room = 1 
                    time.sleep(0.5)
                elif arrowright.rect.collidepoint(pygame.mouse.get_pos()):
                    room = 3
                    time.sleep(0.5)
                # Check if clicking on torch. if yes, add to inventory
                if "TORCH" not in inventory:
                    time.sleep(0.25)
                    if torch_room2.rect.collidepoint(pygame.mouse.get_pos()) or torch2_room2.rect.collidepoint(pygame.mouse.get_pos()):
                        torch_room2.add(inventory)
                        torch_room2.infoadd(inventoryinfo)
                        torch_room2.objectCollected = True
                    
                if "TORCH2" in inventory:
                    if door_room2.rect.collidepoint(pygame.mouse.get_pos()):
                        room = 6 
        # ROOM 3 
        elif room == 3: 
            room3 = Backdrop()
            room3.roomImage = pygame.image.load("images\\room3.png")
            room3.draw(screen)

            # DRAW FLAVOUR TEXT FOR ROOM
            if room3.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(placeholder, [0,480])
                rendertext = font.render("*You are in a desolate library.", 'BLACK', True)
                screen.blit(rendertext, [12,500])

            # DRAW INTERACTIVES
            #basement door
            basement_room3 = Object()
            basement_room3.objectImage = pygame.image.load("images\\basement_room3.png")
            basement_room3.x = 942
            basement_room3.y = 326
            basement_room3.draw(screen)

            #room3 key
            key_room3 = Object()
            key_room3.objectImage = pygame.image.load("images\\key_room3.png")
            key_room3.objectPurpose = "KEY2"
            key_room3.objectName = "key_room3"
            key_room3.x = 548
            key_room3.y = 354
            key_room3.rect = key_room3.objectImage.get_rect(topleft = (key_room3.x, key_room3.y))

            if skullPlaced == True and "KEY2" not in inventory:
                key_room3.draw(screen)

            #pedestals
            pedestal2_room3 = Object()
            if skullPlaced == False:
                pedestal2_room3.objectImage = pygame.image.load("images\\pedestal_room3.png")
                pedestal2_room3.x = 768
                pedestal2_room3.y = 240
            if skullPlaced == True:
                pedestal2_room3.objectImage = pygame.image.load("images\\pedestalskull_room3.png")
                pedestal2_room3.x = 768
                pedestal2_room3.y = 192
            pedestal2_room3.draw(screen)

            # TORCHES
            torch3_room3 = Object()
            torch3_room3.objectPurpose = "TORCH"
            torch3_room3.objectName = "torch_room2"
            torch3_room3.x = 144
            torch3_room3.y = 144
            torch3_room3.draw(screen)
            
            torch4_room3 = Object()
            torch4_room3.objectPurpose = "TORCH"
            torch4_room3.objectName = "torch_room2"
            if "TORCH" not in inventory:
                torch4_room3.x = 96
                torch4_room3.y = 144
                torch4_room3.draw(screen)

            # DRAW ARROWS AND CHECK IF THEY'RE BEING CLICKED
            UI = DrawUI()
            UI.drawleft(screen)
            if "TORCH" in inventory:
                UI.drawright(screen)


            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrowleft.rect.collidepoint(pygame.mouse.get_pos()):
                    room = 2
                    time.sleep(0.5)
                
                if "TORCH" not in inventory:
                    time.sleep(0.25)
                    if torch3_room3.rect.collidepoint(pygame.mouse.get_pos()) or torch4_room3.rect.collidepoint(pygame.mouse.get_pos()):
                        torch_room2.add(inventory)
                        torch_room2.infoadd(inventoryinfo)
                        torch_room2.objectCollected = True

                if "TORCH" in inventory:
                    if arrowright.rect.collidepoint(pygame.mouse.get_pos()):
                        room = 4
                        time.sleep(0.5)
                    if basement_room3.rect.collidepoint(pygame.mouse.get_pos()):
                        room = 4
                        time.sleep(0.5)
                if "SKULL" in inventory:
                    if pedestal2_room3.rect.collidepoint(pygame.mouse.get_pos()):
                        skullPlaced = True
                        inventory.remove(skull_room1.objectPurpose)
                        inventoryinfo.remove(skull_room1.objectName)

                if skullPlaced == True:
                    if key_room3.rect.collidepoint(pygame.mouse.get_pos()):
                        time.sleep(0.25)
                        key_room3.add(inventory)
                        key_room3.infoadd(inventoryinfo)

            elif "TORCH" not in inventory and arrowright.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(placeholder, [0,480])
                rendertext = font.render("*It's quite dark down there. Maybe get some light?", 'BLACK', True)
                screen.blit(rendertext, [12,500])

            elif "TORCH" not in inventory and basement_room3.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(placeholder, [0,480])
                rendertext = font.render("*It's quite dark down there. Maybe get some light?", 'BLACK', True)
                screen.blit(rendertext, [12,500])
            
        # ROOM 4
        elif room == 4:
            room4 = Backdrop()
            room4.roomImage = pygame.image.load("images\\room4.png")
            room4.draw(screen)

            # DRAW FLAVOUR TEXT FOR ROOM
            if room4.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(placeholder, [0,480])
                rendertext = font.render("*You are in a dark basement.", 'BLACK', True)
                screen.blit(rendertext, [12,500])

            # DRAW INTERACTIVES
            # KEY
            key_room4 = Object()
            key_room4.objectImage = pygame.image.load("images\\key_room4.png")
            key_room4.objectPurpose = "KEY"
            key_room4.objectName = "key_room4"
            key_room4.x = 1050
            key_room4.y = 350

            if "KEY" not in inventory:
                key_room4.rect = key_room4.objectImage.get_rect(topleft = (key_room4.x, key_room4.y))
                if coffinOpen == False:
                    key_room4.draw(screen)

            # JOURNAL
            book_room4 = Object()
            book_room4.objectImage = pygame.image.load("images\\book_room4.png")
            book_room4.x = 240
            book_room4.y = 240
            book_room4.draw(screen)

            # CHEST
            treasurechestclosed_room4 = Object()
            if chestOpen == False:
                treasurechestclosed_room4.objectImage = pygame.image.load("images\\treasurechestclosed_room4.png")
                treasurechestclosed_room4.x = 1050
                treasurechestclosed_room4.y = 300
            else: 
                treasurechestclosed_room4.objectImage = pygame.image.load("images\\treasurechestopen_room4.png")
                treasurechestclosed_room4.x = 1050
                treasurechestclosed_room4.y = 288        
            treasurechestclosed_room4.draw(screen)

            # FRACTAL GEM
            fractalgem_room4 = Object()
            fractalgem_room4.objectImage = pygame.image.load("images\\fractalgem_room4.png")
            fractalgem_room4.objectPurpose = "FRACTALGEM"
            fractalgem_room4.objectName = "fractalgem_room4"
            fractalgem_room4.x = 1050
            fractalgem_room4.y = 420
            if "FRACTALGEM" not in inventory:
                fractalgem_room4.rect = fractalgem_room4.objectImage.get_rect(topleft = (fractalgem_room4.x, fractalgem_room4.y))
                if chestOpen == True: 
                    time.sleep(0.25)
                    fractalgem_room4.draw(screen)
            # PEDESTAL
            pedestal_room4 = Object()
            pedestal_room4.objectImage = pygame.image.load("images\\pedestal_room4.png")
            pedestal_room4.x = 960
            pedestal_room4.y = 244
            if gemPlaced == False:
                pedestal_room4.rect = pedestal_room4.objectImage.get_rect(topleft = (pedestal_room4.x, pedestal_room4.y))
                pedestal_room4.draw(screen)
            if gemPlaced == True:
                pedestal_room4.objectImage = pygame.image.load("images\\pedestalfractal_room4.png")
                pedestal_room4.draw(screen)
                room = 5
            
            torch2_room4 = Object()
            torch2_room4.objectImage = pygame.image.load("images\\torch2_room4.png")
            torch2_room4.objectPurpose = "TORCH2"
            torch2_room4.objectName = "torch2_room4"
            torch2_room4.x = 192
            torch2_room4.y = 144
            if chestOpen == True and "TORCH2" not in inventory:
                torch2_room4.draw(screen)

            if "KEY2" in inventory:
                torch2_room4.rect = torch2_room4.objectImage.get_rect(topleft = (torch2_room4.x, torch2_room4.y))

            # DRAW ARROWS AND CHECK IF THEY'RE BEING CLICKED
            UI = DrawUI()
            UI.drawleft(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrowleft.rect.collidepoint(pygame.mouse.get_pos()):
                    room = 3
                    time.sleep(0.5)

                if "KEY" not in inventory:
                    if key_room4.rect.collidepoint(pygame.mouse.get_pos()):
                        time.sleep(0.25)
                        key_room4.add(inventory)
                        key_room4.infoadd(inventoryinfo)
                        key_room4.objectCollected = True
                if book_room4.rect.collidepoint(pygame.mouse.get_pos()):
                    time.sleep(0.25)
                    room = 4.5
                
                if "FRACTALGEM" not in inventory and chestOpen == True:
                    if fractalgem_room4.rect.collidepoint(pygame.mouse.get_pos()):
                        fractalgem_room4.add(inventory)
                        fractalgem_room4.infoadd(inventoryinfo)
                        fractalgem_room4.objectCollected = True

                if "KEY" in inventory and "KEY2" not in inventory:
                    if treasurechestclosed_room4.rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(placeholder, [0,480])
                        rendertext = font.render("*You try your key. It's still locked.", 'BLACK', True)
                        screen.blit(rendertext, [12,500])
                if "KEY" not in inventory and "KEY2" not in inventory:
                    if treasurechestclosed_room4.rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(placeholder, [0,480])
                        rendertext = font.render("*It's locked.", 'BLACK', True)
                        screen.blit(rendertext, [12,500])
                if "KEY2" in inventory:
                    if treasurechestclosed_room4.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(chestopen)
                        chestOpen = True
                        room = 4.75

                if "FRACTALGEM" in inventory:
                    if pedestal_room4.rect.collidepoint(pygame.mouse.get_pos()):
                        gemPlaced = True
                if chestOpen == True:
                    if torch2_room4.rect.collidepoint(pygame.mouse.get_pos()):
                        time.sleep(0.25)
                        torch2_room4.add(inventory)
                        torch2_room4.infoadd(inventoryinfo)

        elif room == 4.5:
            journal12_room4 = Backdrop()
            journal12_room4.roomImage = pygame.image.load("images\\journal12_room4.png")
            journal12_room4.draw(screen)
            screen.blit(placeholder, [0,480])
            rendertext = font.render("*You found a journal.", 'BLACK', True)
            screen.blit(rendertext, [12,500])

            if keys[pygame.K_SPACE]:
                room = 4

        elif room == 4.75:
            journal56_room4 = Backdrop()
            journal56_room4.roomImage = pygame.image.load("images\\journal56_room4.png")
            journal56_room4.draw(screen)
            screen.blit(placeholder, [0,480])
            rendertext = font.render("*You found a journal.", 'BLACK', True)
            screen.blit(rendertext, [12,500])

            if keys[pygame.K_SPACE]:
                room = 4

    ##### ENDINGS ######
        elif room == 5: #THE SORT OF BAD ENDING???
            time.sleep(1)
            screen.fill(BLACK)
            titlefont = pygame.font.SysFont(("Lucida Console"), 50)
            rendertext = titlefont.render("WELCOME BACK, LAZARUS.", True, RED)
            secondarytext = font.render("[end]", True, WHITE)
            screen.blit(rendertext, [260, 300])
            screen.blit(secondarytext, [50, 590])
            if keys[pygame.K_SPACE]:
                room = 8
                time.sleep(0.5)


        elif room == 6:
            time.sleep(1)
            outside = Backdrop()
            outside.roomImage = pygame.image.load("images\\outside.png")
            outside.draw(screen)
            rendertext = font.render("The sun is shining.", True, WHITE)
            secondarytext = font.render("It's a beautiful day. [end]", True, WHITE)
            screen.blit(rendertext, [25, 550])
            screen.blit(secondarytext, [25, 600])
            if keys[pygame.K_SPACE]:
                room = 8
                time.sleep(0.25)

        elif room == 7:
            timeending = Backdrop()
            timeending.roomImage = pygame.image.load("images\\timeending.png")
            timeending.draw(screen)
            if keys[pygame.K_SPACE]:
                room = 8
                time.sleep(0.25)

        
        elif room == 8: #final ending screen
            ending = Backdrop()
            ending.roomImage = pygame.image.load("images\\ending.png")
            ending.draw(screen)
            if keys[pygame.K_SPACE]:
                time.sleep(0.25)
                done = True

    # DRAWING INVENTORY ITEMS AND FLAVOUR TEXT
    itemno = 1
    if 1 <= room <= 4.75:
        for i in inventoryinfo:
            drawobject = pygame.image.load(f"images\\{inventoryinfo[itemno-1]}.png")
            # keep the number of objects within the boxes
            if itemno <= 10:
                item = str(inventory[itemno-1])
                screen.blit(drawobject, [96*itemno-72, 560])
            else:
                pass  
            # draw the next image in the inventory
            itemno+=1
        rendertext = font.render(f"{timet}", True, WHITE)
        screen.blit(rendertext, [1050,575])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
