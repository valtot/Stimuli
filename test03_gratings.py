from psychopy import visual, event, core

win = visual.Window(
    size = [400,400],
    units = "pix",
    fullscr = False
)

gr = visual.GratingStim(
    win = win,
    units = "pix",
    size = [50,50]
)

gr_vpos = [150,50,-50,-150]
gr_phase =[0,0.16,0.33,0.5]

for i_phase in range(4):
    gr.phase = gr_phase[i_phase]
    gr.pos = [0, gr_vpos[i_phase]]
    gr.draw()



win.flip()


event.waitKeys()
win.close()