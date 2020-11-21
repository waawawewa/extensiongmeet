import subprocess
import pyautogui
from time import sleep
import pandas as pd
from datetime import datetime
import webbrowser
def sign_in(link):
	#opens the link
	print("inside")
	webbrowser.open(link, new=20)
	print("opening")
	sleep(15)

	#mutes and turns off video
	sleep(10)
	while pyautogui.locateOnScreen('D:\gmbot\joinss.png'):
		if pyautogui.locateOnScreen('D:\gmbot\joinss.png'):
			sleep(2)
			pyautogui.hotkey('ctrl', 'd')
			pyautogui.hotkey('ctrl', 'e')
			print("muted and cam off")
			break
		else: print(".")
	sleep(2)
	while pyautogui.locateOnScreen('D:\gmbot\joinn.png'):
		if pyautogui.locateOnScreen('D:\gmbot\joinn.png'):
			sleep(2)
			pyautogui.hotkey('ctrl', 'd')
			pyautogui.hotkey('ctrl', 'e')
			print("muted and cam off")
			break
		else: print(".")
	sleep(2)
	#clicks join
	print("clicking the join button")
	while pyautogui.locateOnScreen('D:\gmbot\joinss.png'):
		if pyautogui.locateOnScreen('D:\gmbot\joinss.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('D:\gmbot\joinss.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("clicked on join")
			break
		else: print("")
	while pyautogui.locateOnScreen('D:\gmbot\joinn.png'):
		if pyautogui.locateOnScreen('D:\gmbot\joinn.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('D:\gmbot\joinn.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("clicked on join")
			break
		else: print("")
	# if there is a prompt for recording
	while  pyautogui.locateOnScreen('D:\gmbot\joinss.png'):
		if pyautogui.locateOnScreen('D:\gmbot\joinss.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('D:\gmbot\joinss.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("recording granted")
			break
		else: print(".")

	while  pyautogui.locateOnScreen('D:\gmbot\joinn.png'):
		if pyautogui.locateOnScreen('D:\gmbot\joinnn.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('D:\gmbot\joinn.png')
			pyautogui.moveTo(j)
			pyautogui.click()
			print("recording granted")
			break
		else: print(".")
	sleep(5)
	print("5 sec")
	#leaves the meeting automatically if attendees are below 10 AFTER 45 MINS
	while pyautogui.locateOnScreen('D:\gmbot\endd.png'):
		if pyautogui.locateOnScreen('D:\gmbot\whtext.png'):
			sleep(2)
			j = pyautogui.locateOnScreen('D:\gmbot\whtext.png')
			pyautogui.click(j)
			sleep(1)
			pyautogui.click(j)
			pyautogui.moveTo(x=698, y=385)
			print("MEETING LEFT, WAIT FOR NEXT MEETING")
		else: print("no")
	for i in range (0,9):
		sleep(9)
		print("entered for",i)
	#leaves the meeting automatically if attendees are below 10 AFTER 50 MINS
		if pyautogui.locateOnScreen('D:\gmbot\endd.png'):
			if pyautogui.locateOnScreen('D:\gmbot\whtext.png'):
				sleep(2)
				j = pyautogui.locateOnScreen('D:\gmbot\whtext.png')
				pyautogui.click(j)
				sleep(1)
				pyautogui.click(j)
				pyautogui.moveTo(x=698, y=385)
				break
				print("MEETING LEFT, WAIT FOR NEXT MEETING")
			else: print("no")

	
print("I'm Looking for the timetable")

df = pd.read_csv('D:\gmbot\enter.csv')

while True:
	#checking timetable
	now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	if now in str(df['timings']):
		row = df.loc[df['timings'] == now]
		link = str(row.iloc[0,1])
		print(link)
		sign_in(link)
		sleep(5)
		print("you are in")
