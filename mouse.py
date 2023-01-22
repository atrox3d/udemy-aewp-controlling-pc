import pyautogui as pag
import time

# get mouse position
elapsed = 0
start = time.time()
while elapsed < 2:
    position = pag.position()
    print(position, f'{elapsed=}')
    time.sleep(.10)
    end = time.time()
    elapsed = end - start

# change mouse position
time.sleep(1)
pag.moveTo(*position, duration=2)

position = pag.Point(134, 315)
# mouse clicking
pag.click()
pag.click(*position, clicks=2)
pag.doubleClick(*position)
pag.moveTo(*position)
pag.click(button=pag.SECONDARY)

