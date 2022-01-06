#this is here for the purpose of adding code that runs before the player is put in the main menu such as a splash screen or launch options
import pygame
#start playing the background music
pygame.mixer.init()
music = pygame.mixer.Sound('resources/sounds/backgroundMusic.wav')
pygame.mixer.Channel(1).play(music,-1)
pygame.mixer.set_reserved(1)

exec(open('menu.py').read())    #launch the main menu