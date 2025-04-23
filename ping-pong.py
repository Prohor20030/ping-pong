from pygame import *
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, sizeX = 65, sizeY = 65):
        super().__init__()
        self.image = transform.scale(image.load(filename), (sizeX, sizeY))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y >= 0:
            self.rect.x -= self.speed
        if keys_pressed[K_w] and self.rect.y <= 635:
            self.rect.x += self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ping = Player('ping.png', 325, 430, 4)
pong = Player('pong.png', 325, 430, 4)

window = display.set_mode((500, 500))
game = True

clock = time.Clock()

background = transform.scale(image.load('frame.png'), (500, 500))
while game:
    #text_lose = font1.render('Пропущенно:' + str(lost), 1,(123, 243, 13))
    #text = font1.render('Счет:' + str(score), 1,(74, 177, 39))
    if not finish:
        window.blit(background, (0, 0))
        ping.update()
        ping.reset()
        pong.update()
        pong.reset()


    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()

    clock.tick(60)