import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_keydown_events(event,ai_settings,screen,stats,ship,aliens,bullets):
    if event.key==pygame.K_RIGHT:
       ship.moving_right=True
    elif event.key ==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()
    elif event.key==pygame.K_p:
        start_game(ai_settings,screen,stats,ship,aliens,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullets=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullets)



def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key ==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False
def check_play_button(ai_settings,screen,stats,ship,aliens,bullets,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        start_game(ai_settings,screen,stats,ship,aliens,bullets)
      
def start_game(ai_settings,screen,stats,ship,aliens,bullets):
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()

def check_events(ai_settings,screen,stats,ship,aliens,bullets,play_button):
    #响应事件：
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,ship,aliens,bullets)
                
        elif event.type==pygame.KEYUP:
          check_keyup_events(event=event,ship=ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,ship,aliens,bullets,play_button,mouse_x,mouse_y)
        
         
                # if event.key==pygame.K_RIGHT:
                #     ship.rect.centerx+=2
                # elif event.key==pygame.K_LEFT:
                #     ship.rect.centerx-=2
                # elif event.key==pygame.K_UP:
                #      ship.rect.centery-=2
                # elif event.key==pygame.K_DOWN:
                #      ship.rect.centery+=2

def update_screen(ai_setting,screen,stats,ship,bullets,aliens,play_button,sb):
    #每次循环都重新绘制，屏幕
    screen.fill(ai_setting.screen_bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw()
    #让最近绘制的屏幕可见
    pygame.display.flip()
def update_bullet(ai_settings,screen,stats,ship,bullets,aliens,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,aliens,ship,bullets,sb)
  
def check_bullet_alien_collisions(ai_settings,screen,stats,aliens,ship,bullets,sb):
      #检查是否有子弹击中外星人
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_point*len(aliens)
            sb.prep_score()
        
    if len(aliens)==0:
        ai_settings.increase_speed()
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    #有飞船和外星人相撞
    if stats.ships_left>0:
        stats.ships_left-=1
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
    #清空外星人和子弹
    aliens.empty()
    bullets.empty()
    #创建新的外星人
    create_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()
    #暂停
    

def update_aliens(ai_settings,aliens,ship,stats,screen,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    #改变外星人的方向
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aline_x=int(available_space_x/(2*alien_width))
    return number_aline_x
def get_number_alien_y(ai_settings,ship_height,alien_height):
    #计算可以容纳多少行
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_aline(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    alien.rect.x=alien.x
    aliens.add(alien)
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    #检查是否有外型到达底部
    screen_rect=screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def create_fleet(ai_settings,screen,aliens,ship):
    #创建一群外星人
    alien=Alien(ai_settings,screen)
    number_aline_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_alien_y(ai_settings,ship.rect.height,alien.rect.height)
   #计算一行容纳几个外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aline_x):
            #创建外星人并加入其中
            create_aline(ai_settings,screen,aliens,alien_number,row_number)
            

