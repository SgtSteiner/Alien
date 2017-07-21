# -*- coding: utf-8 -*-
'''
Created on 21 jul. 2017

@author: Steiner
'''

import sys

import pygame

def run_game():
    """ Initilize game and create a screen object """
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # Start the main loop for the game
    while True:
        
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Make the most recently draw screen visible
        pygame.display.flip()
        
run_game()
    