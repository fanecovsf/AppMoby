import PySimpleGUI as sg

#Layouts
#-------------------------------------------------------------------------------------------------------------------------------------------------

LAYOUT_EXEMPLO = [
            [sg.Push(), sg.Text('Bem vindo! Insira o email e senha abaixo para realizar o login', pad=(10,10)), sg.Push()],
            [sg.Push(), sg.Text('Email:   ',pad=(10,10)), sg.Input(size=(30,0), key='email'), sg.Push()],
            [sg.Push(), sg.Text('Senha:  ',pad=(10,10)), sg.Input(size=(30,0),key='password', password_char='*'), sg.Push()],
            [sg.Button('Registro de usuário', pad=(10,15), size=(15,0)), sg.Button('Login', pad=(10,10), size=(15,0)), sg.Button('Sair', pad=(10,10), size=(15,0))],
            [sg.Text('teste')]
        ]