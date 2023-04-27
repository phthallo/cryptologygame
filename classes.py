import pygame
pygame.init()
import time
import threading 
from time import sleep

global inventory
inventory = []
inventoryinfo = []
##### RANDOM #####
##### BACKDROP CLASS  FOR BACKGROUNDS#####
class Backdrop():
    def __init__(self):
        self.roomImage = pygame.image.load("images\\start_screen.png")
        self.x = 0
        self.y = 0

    def draw(self, screen):
        self.rect = self.roomImage.get_rect(topleft = (self.x, self.y))
        drawbg = self.roomImage
        screen.blit(drawbg, [self.x,self.y])

##### MENU CLASS - FOR OTHER RANDOM STUFF #####
class Menu():
    def __init__(self):
        self.menuImage = pygame.image.load("images\\title.png")
        self.menuPurpose = " "
        self.roomNo = 0
        self.x = 200
        self.y = 100

    def draw(self, screen):
        self.rect = self.menuImage.get_rect(topleft = (self.x, self.y))
        drawmenu = self.menuImage
        screen.blit(drawmenu, [self.x, self.y])
    

##### TOGGLE CLASS - FOR BUTTONS #####
class Toggle():
    def __init__(self):
        self.toggleImage = pygame.image.load("images\\start.png")
        self.togglePurpose = " "
        self.roomNo = 0
        self.x = 500
        self.y = 350

    def draw(self, screen):
        self.rect = self.toggleImage.get_rect(topleft = (self.x, self.y))
        drawtoggle = self.toggleImage
        screen.blit(drawtoggle, [self.x, self.y])

##### OBJECT CLASS - FOR OBJECTS ADDED TO INVENTORY #####
class Object():
    def __init__(self):
        self.objectImage = pygame.image.load("images\\torch_room2.png")
        self.objectPurpose = " "
        self.objectName = " "
        self.objectCollected = False
        self.roomNo = 1
        self.x = 480
        self.y = 144
    
    def draw(self, screen):
        self.rect = self.objectImage.get_rect(topleft = (self.x, self.y))
        drawobject = self.objectImage
        screen.blit(drawobject, [self.x, self.y])

    def add(self, inventory):
        inventory.append(f"{self.objectPurpose}")

    def infoadd(self, inventoryinfo):
        inventoryinfo.append(f"{self.objectName}")



