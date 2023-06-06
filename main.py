import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PySimpleGUI as sg
import util.commands as command
import classes.layouts.layoutPattern as pattern
from util.util import Util as util

#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------------------
APP_NAME = 'MobyApp'

STATIC_PATH = os.path.dirname(os.path.abspath(__file__)) + '\static'

ICON = STATIC_PATH + '\Símbolo.ico'

LOGO = STATIC_PATH + '\logo.png'

THEME = 'DarkTeal12'

VERSION = 'Versão alpha 0.01'


#Windows
#-------------------------------------------------------------------------------------------------------------------------------------------------
class WindowPattern:
    def __init__(self):
        self.theme = sg.theme(THEME)


class Login(WindowPattern):
    def __init__(self):
        super().__init__()

        layout = pattern.login()
        window = sg.Window(APP_NAME, layout, icon=ICON)

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED or event == 'Sair':
                break

            elif event == 'Login':
                if command.Select.login_authentication(self.value['email'], self.value['password']):
                    window.close()
                    Register()
                else:
                    util.standardPopup('Email e/ou senha inválidos.')


class Register(WindowPattern):
    def __init__(self):
        super().__init__()

        layout = pattern.register()
        window = sg.Window(APP_NAME, layout, icon=ICON)

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED:
                break


        


#Execução
#-------------------------------------------------------------------------------------------------------------------------------------------------
Login()
