import pyautogui
import time


# duration is in seconds


while (true):
    moveNorth(10)
    moveEast(3)
    moveSouth(10)
    moveEast(3)


def moveNorth(duration):
    move('w')

def moveSouth(duration):
    move('s')

def moveEast(duration):
    move('d')

def moveWest(duration):
    move('a')


def move(key):
    print('Pressing down: ' + key);
    keyDown(key)
    sleep(duration)
    keyUp(key)
