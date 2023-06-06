import PySimpleGUI as sg
import os

#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------------------
APP_NAME = 'MobyApp'

STATIC_PATH = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))) + '\static'

ICON = STATIC_PATH + '\Símbolo.ico'

LOGO = STATIC_PATH + '\logo.png'

THEME = 'DarkTeal12'

VERSION = 'Versão alpha 0.01'


#Classes
#-------------------------------------------------------------------------------------------------------------------------------------------------

class Util:
    def standardPopup(text):
        sg.popup(text, auto_close=True, auto_close_duration=5, title='Erro', icon=ICON)