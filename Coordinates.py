import pyautogui, time

pyautogui.FAILSAFE = True


time.sleep(5)

try:
    while True:
        time.sleep(3)
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(positionStr)

except KeyboardInterrupt:
    print('\n')
