from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def fill_row():
    turn_east()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    put_beeper()


def turn_west():
    while not_facing_west():
        turn_left()

def turn_north():
    while not_facing_north():
        turn_left()

def turn_east():
    while not_facing_east():
        turn_left()

def get_to_next_row():
    turn_west()
    while front_is_clear():
        move()
    turn_north()
    move()


def main():
    while front_is_clear():
        fill_row()
        get_to_next_row()
    fill_row()




# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()