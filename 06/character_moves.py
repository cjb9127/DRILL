from pico2d import *
from math import *
open_canvas()
# 사각형 운동과 원운동이 번갈아 가면서 무한 반복
grass = load_image('grass.png')
character = load_image('character.png')

def move_rectangle():
    x = 400
    y = 90
    while x <= 750:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 3
        delay(0.01)

    while y <= 550:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y += 3
        delay(0.01)

    while x >= 50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= 3
        delay(0.01)

    while y >= 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y -= 3
        delay(0.01)

    while x <= 400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 3
        delay(0.01)
        
def move_circle():
    radian = 0
    x,y = 400,90
    while radian <= 2* math.pi:
        clear_canvas_now()
        grass.draw_now(400,30)
        x = 400 - 210 * sin(radian) #230은 반지름
        y = 300 - 210 * cos(radian)
        character.draw_now(x,y)
        radian += 2 * math.pi / 360
        delay(0.01)

#실행 공간

grass.draw_now(400,30)
character.draw_now(400,90)

while (True):
    move_rectangle()
    delay(0.5)
    move_circle()
    delay(0.5)
    
close_canvas()
