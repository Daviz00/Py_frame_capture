import pyautogui
import time
import winsound
time.sleep(1)
pyautogui.click(625, 1063)

for i in range(162):
    try:
        im = pyautogui.screenshot(region=(273, 119, 1434, 869))
        im.save('HLC_' + str(i) + '.png')
        time.sleep(0.2)
        pyautogui.click(1819, 569)
        time.sleep(0.1)
    except IOError:
        im = pyautogui.screenshot(region=(273, 119, 1434, 869))
        im.save('HLC_' + str(i) + '.png')
        time.sleep(0.2)
        pyautogui.click(1819, 569)
        time.sleep(0.1)
frequency = 4000
duration = 3000
winsound.Beep(frequency, duration)
