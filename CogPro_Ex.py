#Research Design
#Step 0: take the user information (Name initials, age) done 
#Step 1: Instruction window 
##get a user response (any key) to start the experiment 
#Step 2: Present the random alphabets as stimuli in sets of 12 except I, Q, O, S in-process
#Step 3: Also include two numbers from 2-9 in between the set of 12 alphabets 
##vary the alphabets between the two numbers by 1, 2, 3, 4, 5
##each letter/number to be presented for 88ms and an ISI of 32 ms
#Step 4: add music 
#Step 5: recall phase

from psychopy import visual, core, gui, data, event
import random
expName = 'Attentional Blink Experiment'
expInfo = {'Participant':'', 'Session':'','Age':''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False,title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()


win1 = visual.Window(size=[800,600],pos=None,color= (0,0,0))
#st1 = visual.TextStim(win1, text=str('hey'), pos=(0.0,0.0),height=0.5)
#st1.draw()
#win1.flip()
#core.wait(4.0)

alphaStim = ["A", "B", "C", "D", "E", "F", "G", "H",
"J", "K", "L", "M", "N", "P", "R", "T", "U", "V", 
"W", "X", "Y", "Z"]

alphaStimR= random.shuffle(alphaStim)

for i in alphaStim: 
    stimu = visual.TextStim(win1, text=i, bold=True, height=0.8)
    stimu.draw()
    win1.flip()
    core.wait(1.0)
    
win1.close()

