from karel.stanfordkarel import *

def turn_around():
    for i in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def fill_row_with_beepers():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def turn_east():
    while not_facing_east():
        turn_left()

def main():
    fill_row_with_beepers()
    pick_beeper()
    turn_around()
    move_to_wall()

    while beepers_present():
        pick_beeper()
        turn_around()
        move()
        while beepers_present():
            move()
        if no_beepers_present():
            turn_around()
            move()
            turn_around()

    put_beeper()
    turn_east()

if __name__ == '__main__':
    main()