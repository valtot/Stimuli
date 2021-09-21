from psychopy import visual, core
from psychopy import event

win = visual.Window(size = [500,500], fullscr = False, color = [0,0,0])
text = visual.TextStim(win = win, text = 'hello world!',color = [-1,-1,-1], units='pix')

text.draw()
event.waitKeys()
text.color = [-1,0,-1]
text.pos = [2,2]
text.draw()
win.flip() #clearly important command: flips hypothetical background layer on which things are drawn
#core.wait(1.0)

event.waitKeys()
win.close()
