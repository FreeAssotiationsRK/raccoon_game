import time
import math
import pygame as pg
from random import randint


class Dice:
    def __init__(self):
        self.dice = {
            1: (pg.image.load("image/DICE/dice_1.png"), pg.image.load("image/DICE/dice_1.png").get_rect()),
            2: (pg.image.load("image/DICE/dice_2.png"), pg.image.load("image/DICE/dice_2.png").get_rect()),
            3: (pg.image.load("image/DICE/dice_3.png"), pg.image.load("image/DICE/dice_3.png").get_rect()),
            4: (pg.image.load("image/DICE/dice_4.png"), pg.image.load("image/DICE/dice_4.png").get_rect()),
            5: (pg.image.load("image/DICE/dice_5.png"), pg.image.load("image/DICE/dice_5.png").get_rect()),
            6: (pg.image.load("image/DICE/dice_6.png"), pg.image.load("image/DICE/dice_6.png").get_rect()),
        }
        self.random_step = self.dice[randint(1, 6)][0]



