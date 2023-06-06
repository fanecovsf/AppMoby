import PySimpleGUI as sg
import sys
import os
sys.path.insert(0, (os.path.dirname(os.path.abspath(__file__))))

import util.commands as command

#Parameters
#-------------------------------------------------------------------------------------------------------------------------------------------------
CARGOS = [
    'Assistente',
    'Analista',
    'Líder',
    'Gestor'
]

LISTA_PROJETOS = [item for tuple in command.Select.projects_list() for item in tuple]

#Patterns
#-------------------------------------------------------------------------------------------------------------------------------------------------

#Login screen
def login():
    layout = [
                [sg.Push(), sg.Text('Bem vindo! Insira o email e senha abaixo para realizar o login', pad=(10,10)), sg.Push()],
                [sg.Push(), sg.Text('Email:   ',pad=(10,10)), sg.Input(size=(30,0), key='email'), sg.Push()],
                [sg.Push(), sg.Text('Senha:  ',pad=(10,10)), sg.Input(size=(30,0),key='password', password_char='*'), sg.Push()],
                [sg.Button('Registro de usuário', pad=(10,15), size=(15,0)), sg.Button('Login', pad=(10,10), size=(15,0)), sg.Button('Sair', pad=(10,10), size=(15,0))],
                [sg.Text('teste')]
            ]
    return layout


#Register screen
def register():
    layout = [
            [sg.Push(), sg.Text('Registro de usuário',pad=(10,10)), sg.Push()],
            [sg.Push(), sg.Text('E-mail:                   ',pad=(10,10)), sg.Input(size=(30,0), key='register_email'), sg.Push()],
            [sg.Push(), sg.Text('Senha:                    ',pad=(10,10)), sg.Input(size=(30,0), key='register_password', password_char='*'), sg.Push()],
            [sg.Push(), sg.Text('Confirme sua senha:',pad=(10,10)), sg.Input(size=(30,0), key='confirm_password', password_char='*'), sg.Push()],
            [sg.Push(), sg.Text('Cargo:                    ',pad=(10,10)), sg.Combo(CARGOS, size=(28,0), key='register_cargo', readonly=True), sg.Push()],
            [sg.Push(), sg.Text('Projeto:                  ',pad=(10,10)), sg.Combo(LISTA_PROJETOS, size=(28,0), key='register_project', readonly=True), sg.Push()],
            [sg.Button('Voltar', pad=(10,15), size=(15,0)), sg.Push(), sg.Button('Registrar', pad=(10,0), size=(15,0))]
        ]
    
    return layout
