from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def turn_north():
    while not_facing_north():
        turn_left()

def turn_west():
    while not_facing_west():
        turn_left()

def turn_east():
    while not_facing_east():
        turn_left()

def turn_south():
    while not_facing_south():
        turn_left()

def stack_beepers():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def move_to_next_column():
    turn_east()
    for i in range(4):
        move()

def main():
    turn_north()
    stack_beepers()
    move_to_next_column()
    turn_south()
    stack_beepers()
    move_to_next_column()
    turn_north()
    stack_beepers()
    move_to_next_column()
    turn_south()
    stack_beepers()
    turn_east()

if __name__ == '__main__':
    main()