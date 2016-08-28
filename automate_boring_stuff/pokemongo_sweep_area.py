from pyautogui import *
import time


# duration is in seconds


def moveNorth(duration):
    move('w', duration)

def moveSouth(duration):
    move('s', duration)

def moveEast(duration):
    move('d', duration)

def moveWest(duration):
    move('a', duration)


def move(key, duration):
    print('Pressing down: ' + key);
    keyDown(key)
    time.sleep(duration)
    keyUp(key)


while (True):
    moveNorth(20)
    moveEast(8)
    moveSouth(20)
    moveEast(8)


