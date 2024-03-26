import pygame
class Ship ():
    #初始化并设置其位置
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像并获得其外接矩形
        self.image_new=pygame.image.load('ship.bmp')
        self.image=pygame.transform.scale(self.image_new,(60,60))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #飞船在屏幕底部
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.rect.centerx-=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery+=self.ai_settings.ship_speed_factor
        #self.rect.centerx=self.center
    def center_ship(self):
        #让飞船在屏幕中央
        self.rect.bottom=self.screen_rect.bottom


    def blitme(self):
        #绘制飞船
        self.screen.blit(self.image,self.rect)

        