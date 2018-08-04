import pygame

#initialize
pygame.init()

pygame.display.set_caption("Pong Game")

#Set up game window
SIZE = (600, 600)
BG_COLOR = (66, 244, 223)
canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

paddle_image = pygame.image.load("assets/paddle.png")

ball_image = pygame.image.load("assets/ball.png")

x1 = 0
y1 = 100
x2 = 570
y2 = 200

ball_x = 300
ball_y = 300
ball_v_x = 2
ball_v_y = -2


w_pressed = False
s_pressed = False
p_pressed = False
l_pressed = False

loop = True

while loop :
    # pooling
    events = pygame.event.get()
    for e in events :
        if e.type == pygame.QUIT :
            loop = False # action => exit game
        elif e.type == pygame.KEYDOWN :
            if e.key == pygame.K_w :
                w_pressed = True
            if e.key == pygame.K_s :
                s_pressed = True
            if e.key == pygame.K_p :
                p_pressed = True
            if e.key == pygame.K_l :
                l_pressed = True
        elif e.type == pygame.KEYUP :
            if e.key == pygame.K_w :
                w_pressed = False
            if e.key == pygame.K_s :
                s_pressed = False
            if e.key == pygame.K_p :
                p_pressed = False
            if e.key == pygame.K_l :
                l_pressed = False
    if w_pressed :
        y1 -= 5
    if s_pressed :
        y1 += 5
    if p_pressed :
        y2 -= 5
    if l_pressed :
        y2 += 5

    #ball_x += 2
    #ball_y += 0

    #ball_x += -2
    #ball_y += 0

    #ball_x += 0
    #ball_y += 2

    #ball_x += 0
    #ball_y += -2

    #ball_x += -2
    #ball_y += -2

    #ball_x += 2
    #ball_y += 2

    #ball_x += 2
    #ball_y += -2

    ball_x += ball_v_x
    ball_y += ball_v_y



    if ball_x >= 570 or ball_x <= 0 :
        ball_v_x = -ball_v_x
    if ball_y >= 570 or ball_y <= 0 :
        ball_v_y = -ball_v_y




    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image, (x2, y2))
    canvas.blit(ball_image, (ball_x, ball_y))

    clock.tick(60)
    pygame.display.flip()



