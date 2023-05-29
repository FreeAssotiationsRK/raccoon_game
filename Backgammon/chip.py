import pygame as pg


class Chip:
    def __init__(self):
        self.chipsW = {
            1: ((pg.image.load("image/white/white_1.png")), (pg.image.load("image/white/white_1.png").get_rect())),
            2: ((pg.image.load("image/white/white_2.png")), (pg.image.load("image/white/white_3.png").get_rect())),
            3: ((pg.image.load("image/white/white_3.png")), (pg.image.load("image/white/white_3.png").get_rect())),
            4: ((pg.image.load("image/white/white_4.png")), (pg.image.load("image/white/white_4.png").get_rect())),
            5: ((pg.image.load("image/white/white_5.png")), (pg.image.load("image/white/white_5.png").get_rect())),
            6: ((pg.image.load("image/white/white_6.png")), (pg.image.load("image/white/white_6.png").get_rect())),
            7: ((pg.image.load("image/white/white_7.png")), (pg.image.load("image/white/white_7.png").get_rect())),
            8: ((pg.image.load("image/white/white_8.png")), (pg.image.load("image/white/white_8.png").get_rect())),
            9: ((pg.image.load("image/white/white_9.png")), (pg.image.load("image/white/white_9.png").get_rect())),
            10: ((pg.image.load("image/white/white_10.png")), (pg.image.load("image/white/white_10.png").get_rect())),
            11: ((pg.image.load("image/white/white_11.png")), (pg.image.load("image/white/white_11.png").get_rect())),
            12: ((pg.image.load("image/white/white_12.png")), (pg.image.load("image/white/white_12.png").get_rect())),
            13: ((pg.image.load("image/white/white_13.png")), (pg.image.load("image/white/white_13.png").get_rect())),
            14: ((pg.image.load("image/white/white_14.png")), (pg.image.load("image/white/white_14.png").get_rect())),
            15: ((pg.image.load("image/white/white_15.png")), (pg.image.load("image/white/white_15.png").get_rect()))
        }
        self.chipsB = {
            1: ((pg.image.load("image/black/1.png")), (pg.image.load("image/black/1.png").get_rect())),
            2: ((pg.image.load("image/black/2.png")), (pg.image.load("image/black/3.png").get_rect())),
            3: ((pg.image.load("image/black/3.png")), (pg.image.load("image/black/3.png").get_rect())),
            4: ((pg.image.load("image/black/4.png")), (pg.image.load("image/black/4.png").get_rect())),
            5: ((pg.image.load("image/black/5.png")), (pg.image.load("image/black/5.png").get_rect())),
            6: ((pg.image.load("image/black/6.png")), (pg.image.load("image/black/6.png").get_rect())),
            7: ((pg.image.load("image/black/7.png")), (pg.image.load("image/black/7.png").get_rect())),
            8: ((pg.image.load("image/black/8.png")), (pg.image.load("image/black/8.png").get_rect())),
            9: ((pg.image.load("image/black/9.png")), (pg.image.load("image/black/9.png").get_rect())),
            10: ((pg.image.load("image/black/10.png")), (pg.image.load("image/black/10.png").get_rect())),
            11: ((pg.image.load("image/black/11.png")), (pg.image.load("image/black/11.png").get_rect())),
            12: ((pg.image.load("image/black/12.png")), (pg.image.load("image/black/12.png").get_rect())),
            13: ((pg.image.load("image/black/13.png")), (pg.image.load("image/black/13.png").get_rect())),
            14: ((pg.image.load("image/black/14.png")), (pg.image.load("image/black/14.png").get_rect())),
            15: ((pg.image.load("image/black/15.png")), (pg.image.load("image/black/15.png").get_rect()))
        }
