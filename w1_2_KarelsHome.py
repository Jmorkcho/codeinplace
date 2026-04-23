from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.

def turn_south():
    while not_facing_south():
        turn_left()

def turn_east():
    while not_facing_east():
        turn_left()

def turn_west():
    while not_facing_west():
        turn_left()

def turn_north():
    while not_facing_north():
        turn_left()

def main():
    for i in range(2):
        move()
    turn_south()
    move()
    turn_east()
    move()
    pick_beeper()
    turn_west()
    for i in range(3):
        move()
    turn_north()
    move()
    turn_east()
    
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()