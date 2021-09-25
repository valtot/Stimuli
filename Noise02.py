from psychopy import visual, event
import random
import numpy as np


win = visual.Window(
    size = [400,400],
    units = 'pix',
    fullscr = False
)


noise1 = noise = visual.NoiseStim(
    win=win,
    name='noise',
    noiseImage='testImg.jpg',
    units='pix',
    mask='circle',
    ori=1.0, pos=(0, 0),
    size=(512, 512),
    sf=None, phase=0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1, blendmode='add', contrast=1.0,
    texRes=512, filter='None', imageComponent='Phase', noiseType='Gabor',
    noiseElementSize=4, noiseBaseSf=8.0/512, noiseBW=1.0, noiseBWO=30,
    noiseFractalPower=-1,noiseFilterLower=3/512, noiseFilterUpper=8.0/512.0,
    noiseFilterOrder=3.0, noiseClip=3.0, interpolate=False, depth=-1.0
    )


#noise = visual.NoiseStim(
#    win = win,
#    name = 'noise',
#    units = 'pix'
#)


noise1.draw()
win.flip()
event.waitKeys()
win.close()