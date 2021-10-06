from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 640, 512
# 
def quit_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


def follow_hand(X, Y):
    global x, y
    global frames
    disX = (X - x) / 100
    disY = (Y - y) / 100
    for i in range(0,100):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        hand.draw(pos_x, pos_y)
        if (disX > 0):
            character.clip_draw(frames * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_draw(frames * 100, 0, 100, 100, x, y)
        update_canvas()
        frames = (frames + 1) % 8
        x += disX
        y += disY
        delay(0.01)


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frames = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    pos_x = random.randint(0 + 5, KPU_WIDTH - 5)
    pos_y = random.randint(0 + 5, KPU_HEIGHT - 5)
    hand.draw(pos_x, pos_y)
    follow_hand(pos_x, pos_y)
    delay(1)
    quit_events()

close_canvas()




