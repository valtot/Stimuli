from psychopy import visual, core, event
import random

from psychopy.tools.monitorunittools import _height2pix

win = visual.Window(
    size= [400,400],
    pos = [300,0],
    units = 'pix',
    fullscr= False,
    color = [0,0,0]
)

rect = visual.Rect(
    win = win,
    units = 'pix'
)

n_rect = 200

for i in range(n_rect):
    rect.width = random.uniform(10,100)
    rect.height = random.uniform(10,100)
    rect_color = random.uniform(-1,+1)

    rect.fillColor = rect_color
    rect.lineColor = rect_color
    rect.pos = [
        random.uniform (-200,200),
        random.uniform(-200,200)
    ]
    rect.draw()


win.flip()

event.waitKeys()
win.close()
