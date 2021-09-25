from psychopy import visual, event
import random
import numpy as np
import math


win = visual.Window(
    [800, 400],
    units = 'deg',
    fullscr = False
)

num_sqr = [8,6]
nsqr_stim = 8
sqr_size = 4
hsize = num_sqr[0]*4
vsize = num_sqr[1]*4
offset = sqr_size/2
h_margin = (hsize/2)-offset
h_coord = np.arange(-h_margin,+h_margin+offset, offset)
v_margin = (vsize/2)-offset
v_coord = np.arange(-v_margin,+v_margin+offset, offset)

sqr_list = [[[i,j] for i in h_coord] for j in v_coord]

sqr_xy =[]
sqr_color = []

dist_thr = 10
sqr_dist = [dist_thr/2]

for sqr in range(nsqr_stim):
    col = np.repeat(np.random.choice([-1,1]),3,axis= 0)
    sqr_color.append(col)

    if sqr == 0:
        sqr_x = np.random.choice(np.arange(len(h_coord))).astype(int)
        sqr_y = np.random.choice(np.arange(len(v_coord))).astype(int)
        sqr_xy.append(sqr_list[sqr_y][sqr_x][:])
    else:
        while all(x>dist_thr for x in sqr_dist):
            sqr_x = np.random.choice(np.arange(len(h_coord))).astype(int)
            sqr_y = np.random.choice(np.arange(len(v_coord))).astype(int)

            sqr_dist = np.array([math.sqrt((sqr_x-x2)**2+(sqr_y-y2)**2) for x2,y2 in sqr_xy])
        
        sqr_xy.append(sqr_list[sqr_y][sqr_x][:])


sqr_stim = visual.ElementArrayStim(
    win= win,
    units = 'deg',
    nElements = nsqr_stim,
    xys = np.array(sqr_xy),
    elementTex = None,
    elementMask = None,
    colors = sqr_color,
    sizes = sqr_size
)

sqr_stim.draw()
win.flip()
event.waitKeys()
win.close()