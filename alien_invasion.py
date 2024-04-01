import pygame
from ship import Ship
from alien import Alien
from setting import Settings
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreborad import ScoreBorad
def run_game():
    #游戏初始化
    pygame.init()
    ai_settings=Settings()
    #创建用与存储子弹的编组
    bullets=Group()
    aliens=Group()
    stats=GameStats(ai_settings)
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    play_button=Button(ai_settings,screen,"Play")
    sb=ScoreBorad(ai_settings,screen,stats)
    ship=Ship(ai_settings=ai_settings,screen=screen)
    gf.create_fleet(ai_settings,screen,aliens,ship)
    #开始游戏循环
    while True :

        #监视键盘和鼠标
        gf.check_events(ai_settings,screen,stats,ship,aliens,bullets,play_button,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullet(ai_settings,screen,stats,ship,bullets,aliens,sb)
            gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets,sb)
        gf.update_screen(ai_settings,screen,stats,ship,bullets,aliens,play_button,sb)

run_game()