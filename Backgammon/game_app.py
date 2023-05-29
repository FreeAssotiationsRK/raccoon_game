import math
import sys
import time
from random import randint
import pygame as pg
from settings import Settings
from chip import Chip
from dice import Dice

ai_setting = Settings()
chip = Chip()
dice = Dice()
dice_1 = dice.dice[6][0]
dice_2 = dice.dice[1][0]
animation_duration = 8.0
animation_running = False
clock = pg.time.Clock()

active_rect = pg.Surface((85, 85))
active_rect.fill((208, 27, 27))


def animation_dice():
    screen = pg.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pg.display.set_caption("Backgammon")
    start = time.time()
    end = start + 15  # Длительность анимации в секундах
    current = time.time() - start
    progress = min(current / animation_duration, 1.0)
    angle_x = progress * 360
    angle_y = progress * 360
    angle_z = progress * 360

    while time.time() < end:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

        screen.blit(ai_setting.bg_image, (0, 0))
        xW, yW = 67, 692
        for k, v in chip.chipsW.items():
            img = v[0]
            screen.blit(img, (xW, yW))
            xW, yW = 67, yW - 41

        xB, yB = 1051, 26
        for k, v in chip.chipsB.items():
            img = v[0]
            screen.blit(img, (xB, yB))
            xB, yB = 1051, yB + 41

        # Отрисовка кубика на экране
        smooth_angle_x = math.sin(math.radians(angle_x)) * 90
        smooth_angle_y = math.sin(math.radians(angle_y)) * 90
        smooth_angle_z = math.sin(math.radians(angle_z)) * 90

        rotate_dice = pg.transform.rotate(dice.dice[randint(1, 6)][0], smooth_angle_x)
        rotate_dice = pg.transform.rotate(rotate_dice, smooth_angle_y)
        rotate_dice = pg.transform.rotate(rotate_dice, smooth_angle_z)

        rotate_dice_2 = pg.transform.rotate(dice.dice[randint(1, 6)][0], smooth_angle_x)
        rotate_dice_2 = pg.transform.rotate(rotate_dice_2, smooth_angle_y)
        rotate_dice_2 = pg.transform.rotate(rotate_dice_2, smooth_angle_z)

        screen.blit(rotate_dice, (ai_setting.screen_width // 2, ai_setting.screen_height // 2))
        screen.blit(rotate_dice_2, ((ai_setting.screen_width // 2) - 100, ai_setting.screen_height // 2))

        pg.display.flip()
        pg.display.update()


def run_game():
    global dice_1, dice_2
    global animation_running
    screen = pg.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pg.display.set_caption("Backgammon")

    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if not animation_running:
                    animation_running = True
                    animation_dice()
                    animation_running = False
                    dice_1 = dice.dice[randint(1, 6)][0]
                    dice_2 = dice.dice[randint(1, 6)][0]

        screen.blit(ai_setting.bg_image, (0, 0))
        xW, yW = 67, 692
        for k, v in chip.chipsW.items():
            img = v[0]
            screen.blit(img, (xW, yW))
            xW, yW = 67, yW - 41

        xB, yB = 1051, 26
        for k, v in chip.chipsB.items():
            img = v[0]
            screen.blit(img, (xB, yB))
            xB, yB = 1051, yB + 41

        screen.blit(active_rect, (67, 504))
        screen.blit(dice_1, (ai_setting.screen_width // 2, ai_setting.screen_height // 2))
        screen.blit(dice_2, ((ai_setting.screen_width // 2) - 100, ai_setting.screen_height // 2))

        pg.display.flip()
        pg.display.update()


run_game()

