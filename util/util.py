import PySimpleGUI as sg
import os
import pandas as pd 

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

        df = pd.read_table(SCHEDULE_PATH, sep='|', header=0)

        df.columns = [col.strip() for col in df.columns]

        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        df.drop(df.loc[df['Nome do agendamento'] == name].index, inplace=True)

        df.to_csv(SCHEDULE_PATH, sep='|')