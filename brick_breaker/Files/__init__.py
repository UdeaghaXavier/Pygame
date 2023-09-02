from globals import *

ball.create_ball()

while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in LEFT:
                speed -= increment
            if event.key in RIGHT:
                speed += increment
            if event.key == pygame.K_SPACE:
                bouncing = True
        if event.type == pygame.KEYUP:
            if event.key in RIGHT:
                speed -= increment
            if event.key in LEFT:
                speed += increment
        if event.type == pygame.MOUSEBUTTONDOWN:

            if menu.pos[0] <= mouse[0] <= menu.pos[0] + menu.pos[2] and menu.pos[1] <= mouse[1] <= menu.pos[1] + \
                    menu.pos[3]:
                menu.btn_img = "play_btn_clicked.png"
                menu.background()
                pygame.display.update()
                menu.btn_img = "play_btn_normal.png"
                time.sleep(.1)
                menu.background()
                pygame.display.update()
                time.sleep(.2)
                started = True

    if not started:
        menu.background()

    if started:
        menu.close()
        if can_draw:
            WIN.fill(PEACH)
            pygame.draw.rect(WIN, LIGHT_BROWN, top)
            # Time.time()
            wall.draw_wall()
            board.draw_board()
            board.move(speed)
            ball.draw_ball()
            heart.draw_heart(lives)

            if not bouncing:
                ball.follow_player()
            if bouncing:
                res = ball.move()
                lives = res[1]
                bouncing = res[0]

        if wall.is_empty():
            can_draw = False
            if not stop:
                stop = True
        if lives < 0:
            can_draw = False
            display.lost()

    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
