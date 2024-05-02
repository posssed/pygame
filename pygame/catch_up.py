from pygame import *


win = display.set_mode((700, 500))
display.set_captoin("Доганялки")

background = transform.scale(image.load("background.png"), (700, 500))

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))

sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))

x1 = 100
y1 = 350
x2 = 350
y2 = 350

game = True
clock = time.Clock()
FPS = 60

key_presed = key.get_pressed

if key_presed[K_UP] and y2 > 5:
    y2 = y2 - 10
if key_presed[K_DOWN] and y2 < 395:
    y2 = y2 + 10
if key_presed[K_LEFT] and x2 > 5:
    x2 = x2 - 10
if key_presed[K_RIGHT] and x2 < 595:
    x2 = x2 + 10

if key_presed[K_w] and y1 < 5:
    y1 = y1 - 10
if key_presed[K_s] and y1 < 395:
    y1 = y1 + 10
if key_presed[K_s] and x1 > 5:
    x1 = x1 - 10
if key_presed[K_s] and x1 < 595:
    x1 = x1 + 10

if (x1 + 80 == x2 or x2+80 == x1) and (y1+100 == y2 or y2 + 100 == y1):
    game = False

while game:
    win.blit(background, (0, 0))
    win.blit(sprite1, (x1, y1))
    win.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
