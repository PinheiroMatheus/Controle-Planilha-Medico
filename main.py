import pandas as pd
import time
import re
from PySimpleGUI import PySimpleGUI as sg

data_atual = time.strftime('%d', time.localtime())
calendario = pd.read_excel('Calendario_Medico.xlsx')
totalPessoas = 4

for dia in calendario['Dia']:

    if len(str(dia)) == 1:
        dia2 = f"0{dia}"

        if str(dia2) == str(data_atual):
            countPessoa = 0
            while countPessoa < totalPessoas:
                countPessoa = countPessoa + 1
                hora = calendario.loc[calendario['Dia'] == int(data_atual), f'Hora{countPessoa}'].values[0]
                pessoa = calendario.loc[calendario['Dia'] == int(data_atual), f'Pessoa{countPessoa}'].values[0]
                print(f'O {pessoa} estara ausente hoje as {hora}')
                
                if str(pessoa) != 'nan' and str(hora) != 'nan':
                    sg.theme('Reddit')
                    layout = [
                        [sg.Text(f'O {pessoa} estara ausente hoje as {hora}')],
                        [sg.Button('Fechar')]
                    ]
                    janela = sg.Window('Lembrete', layout)

                    while True:
                        eventos, valores = janela.read()
                        if eventos == 'Fechar':
                            break
                        if eventos == sg.WINDOW_CLOSED:
                            break
    
    else:
        if str(dia) == str(data_atual):
            countPessoa = 0
            while countPessoa < totalPessoas:
                countPessoa = countPessoa + 1
                hora = calendario.loc[calendario['Dia'] == int(data_atual), f'Hora{countPessoa}'].values[0]
                pessoa = calendario.loc[calendario['Dia'] == int(data_atual), f'Pessoa{countPessoa}'].values[0]
                print(f'O {pessoa} estara ausente hoje as {hora}')
                
                if str(pessoa) != 'nan' and str(hora) != 'nan':
                    sg.theme('Reddit')
                    layout = [
                        [sg.Text(f'O {pessoa} estara ausente hoje as {hora}')],
                        [sg.Button('Fechar')]
                    ]
                    janela = sg.Window('Lembrete', layout)

                    while True:
                        eventos, valores = janela.read()
                        if eventos == 'Fechar':
                            break
                        if eventos == sg.WINDOW_CLOSED:
                            break