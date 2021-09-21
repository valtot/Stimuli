from psychopy import core, visual, event, parallel, data
import pandas
import json
import random, socket, select
import time

conditionsFile  = r'C:\Users\valen\Desktop\trial.csv.xlsx'
cond = data.importConditions(conditionsFile)
print(cond)