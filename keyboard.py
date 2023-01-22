import pyautogui as pag

# get position of mouse on sample.txt in pycharm
# position = pag.position()
# print(position)

# take note of position and create point
sampletxt = pag.Point(x=145, y=356)

# double click sample.txt in pycharm
pag.doubleClick(*sampletxt)

pag.press(['down', 'enter'])
pag.write('hello from pythonautogui\n')

pag.hotkey('ctrl', 'a')
