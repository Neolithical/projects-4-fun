import pgzrun
import code
import time

name_a = input("⭐️ Enter the name of player 1: ")
name_b = input("⭐️⭐️ Enter the name of player 2: ")

try:
    WIDTH = 900
    HEIGHT = 700

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 120
    BALL_SIZE = 30

    paddle_a = Rect((50, (HEIGHT - PADDLE_HEIGHT) // 2), (PADDLE_WIDTH, PADDLE_HEIGHT))
    paddle_b = Rect((WIDTH - 60, (HEIGHT - PADDLE_HEIGHT) // 2), (PADDLE_WIDTH, PADDLE_HEIGHT))

    ball = Rect((WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)



    ball_velocity = [3, 3]

    score_a = 0
    score_b = 0
    MAX_SPEED = 7
    game_over = False
    game_start = False



    def start():
        global game_start
        if score_a >= 0 and score_b >= 0:
            time.sleep(10)

            game_start = True


    def draw():
        screen.fill("gray")
        screen.draw.filled_rect(paddle_a, "red")
        screen.draw.filled_rect(paddle_b, "blue")

        screen.draw.filled_rect(ball, "black")

        screen.draw.text(f"{name_a}: {score_a}", center=(WIDTH // 4, 30), fontsize=50, color="red")
        screen.draw.text(f"{name_b}: {score_b}", center=(WIDTH * 3 // 4, 30), fontsize=50, color="blue")

        if game_over:
            winner_text = f"{name_a} WON !!" if score_a >= 2 else f"{name_b} WON !!"
            screen.draw.text(winner_text, center=(WIDTH // 2, HEIGHT // 2.5), fontsize=75, color="green")


    def update():
        global score_a, score_b, game_over

        if game_over:
            return

        ball.move_ip(ball_velocity[0], ball_velocity[1])

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_velocity[1] = -ball_velocity[1]

        if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
            ball_velocity[0] = -ball_velocity[0]

        if ball.left <= 0:
            score_b += 1
            check_victory()
            reset()

        elif ball.right >= WIDTH:
            score_a += 1
            check_victory()
            reset()

        move_paddles()


    def move_paddles():
        if keyboard.w and paddle_a.top > 0:
            paddle_a.y -= 6

        if keyboard.s and paddle_a.bottom < HEIGHT:
            paddle_a.y += 6

        if keyboard.up and paddle_b.top > 0:
            paddle_b.y -= 6

        if keyboard.down and paddle_b.bottom < HEIGHT:
            paddle_b.y += 6


    def reset():
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_velocity[0] = -ball_velocity[0]

        ball_velocity[0] += 1 if ball_velocity[0] > 0 else -1a
        ball_velocity[1] += 1 if ball_velocity[1] > 0 else -1



        time.sleep(3)



        if abs(ball_velocity[0]) > MAX_SPEED:

            ball_velocity[0] = MAX_SPEED if ball_velocity[0] > 0 else -MAX_SPEED

        if abs(ball_velocity[1]) > MAX_SPEED:

            ball_velocity[1] = MAX_SPEED if ball_velocity[1] > 0 else -MAX_SPEED


    def check_victory():
        global game_over
        if score_a >= 2 or score_b >= 2:
            game_over = True


    def on_quit():
        quit()


    pgzrun.go()

except Exception:
    print("Something went wrong!")

finally:
    print(f'\n👑 I hope you both had fun ‼️')
