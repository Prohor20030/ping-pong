from pygame import *
finish = False

lost = 0
score = 0
class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, sizeX = 14, sizeY = 120):
        super().__init__()
        self.image = transform.scale(image.load(filename), (sizeX, sizeY))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y <= 349:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y >= 33:
            self.rect.y -= self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y <= 349:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y >= 33:
            self.rect.y -= self.speed

speed_x = 3
speed_y = 3

class Ball(GameSprite):

    def update(self):
        global speed_y, speed_x
        self.rect.x += speed_x
        self.rect.y += speed_y
    
        if self.rect.y > 449 or self.rect.y < 33:
            speed_y *= -1
        
        if self.rect.x < 30:
            global lost
            lost += 1
            self.rect.y = 230
            self.rect.x = 230
        if self.rect.x > 453:
            global score
            score += 1
            self.rect.y = 230
            self.rect.x = 230

font.init()
font1 = font.SysFont('Arial', 30)
font2 = font.SysFont('Arial', 30)

win = font2.render('Ю ВОН', True, (54, 128, 72))
lose = font2.render('Ю ЛОСЬ', True, (28, 144, 87))

ping = Player1('ping.png', 30, 50, 4)
pong = Player2('pong.png', 457, 350, 4)
ball = Ball('ping-pong ball.png', 240, 240, 3, 20, 20)

window = display.set_mode((500, 500))
game = True

clock = time.Clock()

background = transform.scale(image.load('frame.png'), (500, 500))
while game:
    text_score1 = font1.render('score:' + str(score), 1,(125, 255, 105))
    text_socre2 = font1.render('score:' + str(lost), 1,(240, 20, 210))
    if not finish:
        window.blit(background, (0, 0))
        window.blit(text_score1, (28, 0))
        window.blit(text_socre2, (360, 0))
        ping.update()
        ping.reset()
        pong.update()
        pong.reset()
        ball.update()
        ball.reset()
        if sprite.collide_rect(ping, ball) or sprite.collide_rect(pong, ball):
           speed_x *= -1
        


    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()

    clock.tick(60)