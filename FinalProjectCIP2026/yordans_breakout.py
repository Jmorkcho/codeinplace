from graphics import Canvas
import random
import time

# Window size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 600

# Brick settings
BRICK_ROWS = 10
BRICK_COLS = 10
BRICK_WIDTH = 35
BRICK_HEIGHT = 15
BRICK_SPACING = 5
BRICK_OFFSET = 50

# Paddle settings
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
PADDLE_Y_OFFSET = 50

# Ball settings
BALL_SIZE = 20

# Game settings
NUM_TURNS = 3
DELAY = 0.01


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Create bricks
    bricks_left = create_bricks(canvas)

    # Create paddle
    paddle = create_paddle(canvas)

    turns = NUM_TURNS

    while turns > 0 and bricks_left > 0:

        # Create a new ball each turn
        ball = create_ball(canvas)

        # Ball velocity
        change_x = random.randint(3, 5)
        if random.random() > 0.5:
            change_x = -change_x

        change_y = 5

        turn_over = False

        while not turn_over and bricks_left > 0:

            # Move paddle with mouse
            mouse_x = canvas.get_mouse_x()

            if mouse_x is not None:
                paddle_x = mouse_x - PADDLE_WIDTH / 2

                # Keep paddle inside window
                if paddle_x < 0:
                    paddle_x = 0

                if paddle_x + PADDLE_WIDTH > CANVAS_WIDTH:
                    paddle_x = CANVAS_WIDTH - PADDLE_WIDTH

                canvas.moveto(
                    paddle,
                    paddle_x,
                    CANVAS_HEIGHT - PADDLE_Y_OFFSET
                )

            # Move ball
            canvas.move(ball, change_x, change_y)

            # Get ball position
            ball_x = canvas.get_left_x(ball)
            ball_y = canvas.get_top_y(ball)

            # Bounce off left/right walls
            if ball_x <= 0 or ball_x + BALL_SIZE >= CANVAS_WIDTH:
                change_x = -change_x

            # Bounce off top wall
            if ball_y <= 0:
                change_y = -change_y

            # Bottom wall = lose turn
            if ball_y + BALL_SIZE >= CANVAS_HEIGHT:
                canvas.delete(ball)
                turn_over = True
                turns -= 1
                break

            # Collision detection
            colliders = canvas.find_overlapping(
                ball_x,
                ball_y,
                ball_x + BALL_SIZE,
                ball_y + BALL_SIZE
            )

            for obj in colliders:

                # Ignore the ball itself
                if obj == ball:
                    continue

                # Paddle collision
                if obj == paddle:

                    # Only bounce if ball is moving downward
                    if change_y > 0:
                        change_y = -change_y

                    break

                # Brick collision
                else:
                    canvas.delete(obj)
                    bricks_left -= 1
                    change_y = -change_y
                    break

            time.sleep(DELAY)

    # End message
    if bricks_left == 0:
        canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            "YOU WIN!",
            font="30px Arial"
        )
    else:
        canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            "GAME OVER",
            font="30px Arial"
        )



def create_bricks(canvas):
    colors = ["red", "red",
              "orange", "orange",
              "yellow", "yellow",
              "green", "green",
              "cyan", "cyan"]

    total_width = (
        BRICK_COLS * BRICK_WIDTH
        + (BRICK_COLS - 1) * BRICK_SPACING
    )

    start_x = (CANVAS_WIDTH - total_width) / 2

    brick_count = 0

    for row in range(BRICK_ROWS):

        y = BRICK_OFFSET + row * (BRICK_HEIGHT + BRICK_SPACING)

        for col in range(BRICK_COLS):

            x = start_x + col * (BRICK_WIDTH + BRICK_SPACING)

            canvas.create_rectangle(
                x,
                y,
                x + BRICK_WIDTH,
                y + BRICK_HEIGHT,
                colors[row],
                colors[row]
            )

            brick_count += 1

    return brick_count


def create_paddle(canvas):
    x = (CANVAS_WIDTH - PADDLE_WIDTH) / 2
    y = CANVAS_HEIGHT - PADDLE_Y_OFFSET

    return canvas.create_rectangle(
        x,
        y,
        x + PADDLE_WIDTH,
        y + PADDLE_HEIGHT,
        "black",
        "black"
    )


def create_ball(canvas):
    x = CANVAS_WIDTH / 2 - BALL_SIZE / 2
    y = CANVAS_HEIGHT / 2 - BALL_SIZE / 2

    return canvas.create_oval(
        x,
        y,
        x + BALL_SIZE,
        y + BALL_SIZE,
        "black",
        "black"
    )


if __name__ == '__main__':
    main()