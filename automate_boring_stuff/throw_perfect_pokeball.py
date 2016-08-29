import pyautogui
import time


# click app from the taskbar
pyautogui.click(631, 1055)

pyautogui.moveTo(1275, 700)


def throw_pokeball(distance):
	# short distance
	if distance == 1:
		pyautogui.dragRel(0, -300, .2, button='left')
	# medium distance
	elif distance == 2: 
		pyautogui.dragRel(0, -400, .2, button='left')
	# far distance
	else:
		pyautogui.dragRel(0, -550, .2, button='left')


throw_pokeball(2)




# click back script
pyautogui.click(1120, 1055)
