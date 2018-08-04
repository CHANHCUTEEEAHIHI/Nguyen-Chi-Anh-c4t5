if ball_y == 580 and ball_x >= 0 and ball_x <= 600:
    ball_v_y = - ball_v_y
if ball_y == 0 and ball_x >= 0 and ball_x <= 600:
    ball_v_y = - ball_v_y
if ball_x <= 30 and ball_y >= y1 and ball_y <= y1 + 120:
    ball_v_x = -ball_v_x
if ball_x >= 550 and ball_y >= y2 and ball_y <= y2 + 120:
    ball_v_x = -ball_v_x
