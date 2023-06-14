import PySimpleGUI as sg
import sys
import os
import pandas as pd


#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------------------
STATIC_PATH = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))) + '\static'

SCHEDULE_PATH = STATIC_PATH + '\schedule.txt'

#Patterns
#-------------------------------------------------------------------------------------------------------------------------------------------------

#Scheduler
def scheduler():
    df = pd.read_table(SCHEDULE_PATH, encoding='UTF-8', sep='|')

    data = df.values.tolist()
    df.columns = [col.strip() for col in df.columns]
    columns = list(df.columns)

    layout = [
        [sg.Push(), sg.Text('Agendamentos', font=('Arial', 20), pad=(20,20), size=(52,0), justification='center'), sg.Push()],
        [sg.Push(), sg.Table(
                            data, 
                            columns,
                            num_rows=20, 
                            auto_size_columns=False, 
                            justification='center', 
                            enable_events=True, 
                            key='-TABLE-', 
                            max_col_width=30, 
                            def_col_width=20, 
                            size=(50,0),
                            vertical_scroll_only=False,
                            ), 
                            sg.Push()],
        [sg.Push(), sg.Button('Sair', size=(20,0)), sg.Button('- Deletar agendamento', size=(20,0)), sg.Button('+ Criar agendamento', size=(20,0)), sg.Push()]
    ]

    return layout

#CreateSchedule
def createSchedule():

    layout = [
        [sg.Text('Nome:', pad=(10,3), justification='left'), sg.Input(key='-NAME-', size=(30,0))],
        [sg.Text('Arquivo:', pad=(10,3), justification='left'),sg.Button('📁', target='-ARCHIVE-', font=('Arial', 12)), sg.Input(key='-RES-', size=(10,0), readonly=True) ,sg.Input(key='-ARCHIVE-', visible=False)],
        [sg.Text('Periodicidade (hh:mm:ss):', pad=(10,3), justification='left'), sg.Input(key='-TIME-', size=(15,0))],
        [sg.Push(),sg.Button('Cancelar', size=(12,0), pad=(5,10)),sg.Button('Criar', size=(12,0), pad=(5,0)), sg.Push()]
    ]

    return layout
