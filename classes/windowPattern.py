import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import PySimpleGUI as sg
import util.commands as command
import layouts.layoutPattern as pattern

#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------------------
APP_NAME = 'MobyApp'

STATIC_PATH = os.path.dirname(os.path.abspath(__file__)) + '\static'

ICON = STATIC_PATH + '\Símbolo.ico'

LOGO = STATIC_PATH + '\logo.png'

THEME = 'DarkTeal12'

VERSION = 'Versão 0.21 - 1º Deploy'


#Patterns
#-------------------------------------------------------------------------------------------------------------------------------------------------

class window:
    def __init__(self, layout):
        sg.theme(THEME)

        self.layout = layout
        self.window = sg.Window(APP_NAME, self.layout, icon=ICON)

        pass


class popupOk:
    def __init__(self, layout, text):
        sg.theme(THEME)
        
        self.text = text
        self.layout = layout
        self.window = sg.Window(APP_NAME, self.layout, icon=ICON)
        pass