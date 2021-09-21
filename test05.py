from random import uniform
from psychopy import visual, event
import random

win = visual.Window(
    size = [400,400],
    pos =[350,350],
    units = 'pix',
    fullscr = True
)

n_dots = 200
dot_xy =[]

for dot in range(n_dots):
    dot_x = random.uniform(-200,200)
    dot_y = random.uniform(-200,200)

    dot_xy.append([dot_x,dot_y])

dot_stim = visual.ElementArrayStim(
    win= win,
    units = 'pix',
    nElements = n_dots,
    xys = dot_xy,
    elementTex = None,
    elementMask = 'circle',
    sizes = 10

)

dot_stim.draw()
win.flip()
event.waitKeys()
win.close()