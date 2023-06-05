from pygame import *

class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y




    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<window_width-80:
            self.rect.y+=self.speed
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<window_width-80:
            self.rect.y+=self.speed


back =(200,255,255)
window_width=600
window_height=500
window=display.set_mode((window_width,window_height))
window.fill(back)

game=True
finish=False
clock=time.Clock()
fps=90

racket1 = Player('racet.png',30,200,50,150,4)
racket2 = Player('racet.png',520,200,50,150,4)
mzx = GameSprite('mzx.png',200,200,50,50,4)

font.init()
font=font.SysFont(None,35)
lose1 = font.render('Player 1 lose', True,(180,0,0))
lose2 = font.render('Player 2 lose', True,(180,0,0))

speed_x=3
speed_y=3



while game:
    for e in event.get():
        if e.type ==QUIT:
            game=False
    if finish!=True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        mzx.rect.x +=speed_x
        mzx.rect.y +=speed_y

        if sprite.collide_rect(racket1,mzx) or sprite.collide_rect(racket2,mzx):
            speed_x*=-1
            speed_y*=-1
        if mzx.rect.y>window_height-50 or mzx.rect.y<0:
            speed_y*=-1
        if mzx.rect.x<0:
            finish=True
            window.blit(lose1,(200,200))
            game_over = True
        if mzx.rect.x>window_width:
            finish=True
            window.blit(lose2,(200,200))
            game_over = True


        racket1.reset()
        racket2.reset()
        mzx.reset()
    display.update()
    clock.tick(fps)

