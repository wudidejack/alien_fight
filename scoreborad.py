import pygame.font
from ship import Ship
from pygame.sprite import Group
class ScoreBorad():
    def __init__(self,ai_settings,screen,stats):
        self.sceen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_height_score()
        self.prep_level()
        self.prep_ship()
    def prep_score(self):
        roound_score=round(self.stats.score,-1)
        score_str="{:,}".format(roound_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.screen_bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    def show_score(self):
        self.sceen.blit(self.score_image,self.score_rect)
        self.sceen.blit(self.height_socre_image,self.height_socre_rect)
        self.sceen.blit(self.level_image,self.level_image_rect)
        self.ships.draw(self.sceen)
    def prep_height_score(self):
        height_score=int(round(self.stats.height_score,-1))
        height_score_str="{:,}".format(height_score)
        self.height_socre_image=self.font.render(height_score_str,True,self.text_color,self.ai_settings.screen_bg_color)
        self.height_socre_rect=self.height_socre_image.get_rect()
        self.height_socre_rect.top=self.screen_rect.top+20
        self.height_socre_rect.centerx=self.screen_rect.centerx
    def prep_level(self):
        self.level_image=self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.screen_bg_color)
        self.level_image_rect=self.level_image.get_rect()
        self.level_image_rect.right=self.score_rect.right
        self.level_image_rect.top=self.score_rect.bottom+20
    def prep_ship(self):
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_settings,self.sceen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)


        