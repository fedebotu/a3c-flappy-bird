import numpy as np
import sys
sys.path.append("game/")

import pygame
import wrapped_flappy_bird as game

import skimage
from skimage import transform, color, exposure

import keras
from keras.models import Sequential, Model, load_model
from keras.layers.core import Dense, Flatten, Activation
from keras.layers.convolutional import Convolution2D
from keras.optimizers import RMSprop
import keras.backend as K
SOUND_ON = True
game_state = game.GameState(30, SOUND_ON)

currentScore = 0
topScore = 0
a_t = [1,0] # not flap
FIRST_FRAME = True
game.showScore(currentScore)

terminal = False
r_t = 0
while True:
    a_t = [1,0]
    if FIRST_FRAME:
    	game_state.getCurrentFrame()
    	FIRST_FRAME = False		

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a_t = [0,1]   
    _, r_t, terminal = game_state.frame_step(a_t)     

    if(r_t == 1):
        currentScore += 1
        game.showScore(currentScore)
        topScore = max(topScore, currentScore)
        print("Current Score: " + str(currentScore) + " Top Score: " + str(topScore))
    
    if terminal == True:
        print("The bird died! You scored: " + str(currentScore))
        print("##############################################")     
        FIRST_FRAME = True
        terminal = False
        currentScore = 0
        game.showScore(currentScore)
				