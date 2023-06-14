import PySimpleGUI as sg
import os

#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------------------
APP_NAME = 'MobyApp'

STATIC_PATH = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))) + '\static'

SCHEDULE_PATH = STATIC_PATH + '\schedule.txt'


#Classes
#-------------------------------------------------------------------------------------------------------------------------------------------------

class Util:
    def standardPopup(text):
        sg.popup(text, auto_close=True, title='Erro')


    def deleteSchedule(name):

        with open(SCHEDULE_PATH, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if name in line:
                del lines[i]
                break


        with open(SCHEDULE_PATH, 'w', encoding='UTF-8') as file:
            file.write(str(lines))