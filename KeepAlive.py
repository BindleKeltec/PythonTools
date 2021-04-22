import pyautogui

pyautogui.FAILSAFE = True
firstposition = 400, 400
secondposition = 300,300
thirdposition = 900,400

minutes = float(input("How many minutes do you want to chill for? "))
moves = minutes*30
for i in range(int(moves)):

	pyautogui.moveTo(firstposition, duration = 1)
	pyautogui.moveTo(secondposition, duration = 1)
	if i %10 == 0:
		pyautogui.moveTo(thirdposition, duration = 1)
		pyautogui.click()
		pyautogui.press('space')