from psychopy import visual, event, core

win = visual.Window(
    size = [400,400],
    units = "pix",
    fullscr = False
)

gr = visual.GratingStim(
    win = win,
    units = "pix",
    size = [150,150]
)

gr.ori = 45

gr.sf = 5.0/150.0
gr.draw()
win.flip()


event.waitKeys()
win.close()