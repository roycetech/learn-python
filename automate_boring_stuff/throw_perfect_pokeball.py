import pyautogui
import time


# click bluestack app from the taskbar
pyautogui.click(pyautogui.locateCenterOnScreen("blue_stacks_task_icon.png"))
# pyautogui.click(1000, 1055)

pyautogui.moveTo(1275, 700)


def throw_pokeball(distance):
	# short distance
	if distance == 1:
		pyautogui.dragRel(0, -300, .2, button='left')
		
	# medium distance
	elif distance == 2: 
		pyautogui.dragRel(0, -400, .2, button='left')

	# medium distance
	elif distance == 3: 
		pyautogui.dragRel(0, -550, .15, button='left')

	# far distance
	else:
		pyautogui.dragRel(0, -500, .25, button='left')


throw_pokeball(3)



# click back script

pyautogui.click(pyautogui.locateCenterOnScreen("sublime2_task_icon.png"))
# pyautogui.click(845, 1055)
