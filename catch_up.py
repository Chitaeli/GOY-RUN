from pygame import *

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('фнуф')

speed = 10
#задай фон сцены
backgroung = transform.scale(
    image.load('fon.jpg'),
    (700,500)
)
#создай 2 спрайта и размести их на сцене
x1 = 500
x2 = 300
y1 = 300
y2 = 300
sprite1 = transform.scale(
    image.load('spr1.png'),
    (100,200)
)

sprite2 = transform.scale(
    image.load('spr2.png'),
    (100,200)
)
#обработай событие «клик по кнопке "Закрыть окно"»
clock = time.Clock()
game = True
while game:
    window.blit(backgroung, (0,0))
    window.blit(sprite1, (x1, y1))
    clock.tick(60)
    window.blit(sprite2, (x2, y2))
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False

#движение персонажа 1
    if keys_pressed[K_UP] and y1>=0:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1<=400:
        y1 += speed
    if keys_pressed[K_LEFT] and x1>=0:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1<=600:
        x1 += speed

    #движение персонажа 2
    if keys_pressed[K_w] and y2>=0:
        y2 -= speed
    if keys_pressed[K_s] and y2<=400:
        y2 += speed
    if keys_pressed[K_a] and x2>=0:
        x2 -= speed
    if keys_pressed[K_d] and x2<=600:
        x2 += speed
    display.update()