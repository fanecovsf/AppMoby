import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PySimpleGUI as sg
import util.commands as command
import classes.layouts.layoutPattern as pattern
from util.util import Util
import pandas as pd
import datetime

#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------------------
APP_NAME = 'MobyApp'

STATIC_PATH = os.path.dirname(os.path.abspath(__file__)) + '\static'

SCHEDULE_PATH = STATIC_PATH + '\schedule.txt'

ICON = STATIC_PATH + '\symbol.ico'

LOGO = STATIC_PATH + '\logo.png'

THEME = 'DarkAmber'

VERSION = 'Versão alpha 0.01'


#Windows
#-------------------------------------------------------------------------------------------------------------------------------------------------
class StartEngine:
    def __init__(self):
        with open(SCHEDULE_PATH, 'a', encoding='UTF-8') as file:

            if file.tell() == 0:
                file.write('Nome do agendamento | Arquivo | Caminho do arquivo | Data de criação | Periodicidade | Execuções | Última execução | Próxima execução\n')
                file.close()
            else:
                pass
            
            pass

        Scheduler()


class WindowPattern:
    def __init__(self):
        self.theme = sg.theme(THEME)


class Scheduler(WindowPattern):
    def __init__(self):
        super().__init__()

        window = sg.Window(APP_NAME, layout=pattern.scheduler(), icon=ICON)

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED or event == 'Sair':
                break

            if event == '+ Criar agendamento':
                window.disable()
                CreateSchedule()
                df = pd.read_table(SCHEDULE_PATH, encoding='UTF-8', sep='|')
                df.columns = [col.strip() for col in df.columns]
                window['-TABLE-'].update(values=df.values.tolist())
                window.enable()
                window.bring_to_front()

            if event == '- Deletar agendamento':

                df = pd.read_table(SCHEDULE_PATH, encoding='UTF-8', sep='|')
                df.columns = [col.strip() for col in df.columns]

                if self.value['-TABLE-'][0] != -1:
                    selected_data = df.loc[self.value['-TABLE-'][0], 'Nome do agendamento']
                    Util.deleteSchedule(selected_data)
                    window['-TABLE-'].update(values=df.values.tolist())


class CreateSchedule(WindowPattern):
    def __init__(self):
        super().__init__()

        window = sg.Window(APP_NAME, layout=pattern.createSchedule(), icon=ICON)

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break

            if event == '📁':
                fullPath = sg.popup_get_file('Selecione um arquivo')
                if fullPath:
                    fileName = os.path.basename(fullPath)
                    window['-RES-'].update(fileName)
                    window['-ARCHIVE-'].update(fullPath)

            if event == 'Criar':
                df = pd.read_table(SCHEDULE_PATH, encoding='UTF-8', sep='|')
                df.columns = [col.strip() for col in df.columns]

                duration = self.value['-TIME-']

                if self.value['-NAME-'] in df['Nome do agendamento'].values or self.value['-NAME-'] == '':
                    sg.popup('Nome inválido ou já existente.', no_titlebar=True)

                elif self.value['-ARCHIVE-'] == '' or '.py' not in self.value['-ARCHIVE-']:
                    sg.popup('Selecione um arquivo válido.', no_titlebar=True)

                elif len(duration.split(':')) != 3:
                    sg.popup('Periodicidade inválida. Insira um tempo válido no formato hh:mm:ss.', no_titlebar=True)

                elif len(duration.split(':')) == 3:
                    try:
                        hour, minutes, seconds = map(int, duration.split(':'))

                        hour_full = str(hour).zfill(2)
                        minutes_full = str(minutes).zfill(2)
                        seconds_full = str(seconds).zfill(2)

                        completeDuration = f"{hour_full}:{minutes_full}:{seconds_full}"

                        y = datetime.datetime.now()
                        formatted_date = y.strftime("%d/%m/%Y %H:%M:%S")

                        firstExecution = y + datetime.timedelta(hours=hour, minutes=minutes, seconds=seconds)
                        firstExecution = firstExecution.strftime("%d/%m/%Y %H:%M:%S")

                        with open(SCHEDULE_PATH, 'a', encoding='UTF-8') as file:
                            file.write(f"{self.value['-NAME-']}|{self.value['-RES-']}|{self.value['-ARCHIVE-']}|{formatted_date}|{completeDuration}|-|-|{firstExecution}\n")
                            file.close()

                        sg.popup('Agendamento criado com sucesso!', no_titlebar=True)
                        break
                        

                    except Exception as e:
                        print(e)
                        sg.popup('Periodicidade inválida. Insira um tempo válido no formato hh:mm:ss.', no_titlebar=True)

#Execução
#-------------------------------------------------------------------------------------------------------------------------------------------------
StartEngine()
