from psychopy import visual, event
import random
import numpy as np


win = visual.Window(
    size = [1920,1080],
    units = 'pix',
    fullscr = True
)

num_sqr = [28,16]
sqr_size = 10

offset = (win.size[0]/(num_sqr[0]))/2

n_sqr = num_sqr[0]*num_sqr[1]
dot_xy =[]
sqr_color = []


for dot in range(n_dots):
    dot_x = random.uniform(-200,200)
    dot_y = random.uniform(-200,200)
    col = np.repeat(np.random.choice([-1,1]),3,axis= 0)
    dot_xy.append([dot_x,dot_y])



dot_stim = visual.ElementArrayStim(
    win= win,
    units = 'pix',
    nElements = n_sqr,
    xys = sqr_xy,
    elementTex = None,
    elementMask = None,
    colors = sqr_color,
    sizes = sqr_size
)

dot_stim.draw()
win.flip()
event.waitKeys()
win.close()