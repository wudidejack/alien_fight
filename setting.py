class Settings():
    def __init__(self):
        #屏幕设置
        self.screen_width=1600
        self.screen_height=1000
        self.screen_bg_color=(230,230,250)
        #飞船设置
        self.ship_limit=3
        #子弹设置
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        #外星人设置
        self.fleet_drop_speed=3
        #分数提高
        self.score_scale=1.5
        self.speeedup_scale=1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        #初始化设置
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        #外星人移动
        self.fleet_direction=1
        #分数
        self.alien_point=50

    
    def increase_speed(self):
        self.ship_speed_factor*=self.speeedup_scale
        self.bullet_speed_factor*=self.speeedup_scale
        self.alien_speed_factor*=self.speeedup_scale
        self.alien_point=int(self.score_scale*self.alien_point)
        print(self.alien_point)


