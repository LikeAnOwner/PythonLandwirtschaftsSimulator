import PySimpleGUI as sg

def startWindow():
    layout = [
        [sg.Text('Python Landwirtschafts Simulator', size=(69, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)],
        [sg.Button('Neues Spiel', key='StartNeuesSpiel')],
        [sg.Button('Mitwirkende', key='StartMitwirkende')],
        [sg.Button('Beenden', key='StartBeenden')]
    ]
    window = sg.Window('Python Landwirtschafts Simulator', layout, size=(720, 480))
    return window

def mitwirkendeWindow():
    layout = [
        [sg.Text('Mitwirkende', size=(69, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)],
        [sg.Text('Jan Ole Nies')],
        [sg.Text('Jakob Jost Becker')],
        [sg.Button('Zurück', key='MitwirkendeZurück')]
    ]
    window = sg.Window('Python Landwirtschafts Simulator', layout, size=(720, 480))
    return window

def gameName():
    layout = [
        [sg.Text('Python Landwirtschafts Simulator', size=(69, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)],
        [sg.Text('Herzlich willkommen zum Python Farming Simulator von Ole und Jakob!')],
        [sg.Text('Du hast den alten Hof deines Großvaters geerbt, doch sehen die Bilanzen leider gar nicht gut aus.')],
        [sg.Text('Um den Hof nun wieder auf Vordermann zu bringen, müssen einige Aufgaben erledigt werden.')],
        [sg.Text('Bevor du richtig loslegen kannst, musst du nur noch die Erburkunde unterschrieben.')],
        [sg.Text('Bitte trag deinen Namen in das Eingabefeld ein und bestätige mit der Eingabetaste.')],
        [sg.InputText(key='username')],
        [sg.Submit('Bestätigen', key='NameBestätigen')],
    ]
    window = sg.Window('Python Landwirtschafts Simulator', layout, size=(720, 480))
    return window

def newGame():
    layout = [
        [sg.Text('Python Landwirtschafts Simulator', size=(69, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)],
        [sg.Text('Nachdem du nun das Rechtliche abgeschlossen hast, kannst du mit der Abarbeitung der Aufgaben loslegen.')],
        [sg.Text('Um eine Auflistung aller Befehle zu erhalten, trage \'hilfe\' in die Konsole ein.')],
        [sg.InputText(key='username')],
        [sg.Submit('Bestätigen', key='NameBestätigen')],
    ]
    window = sg.Window('Python Landwirtschafts Simulator', layout, size=(720, 480))
    return window

def startGame():
    window = startWindow()
    while True:
        event, values = window.read()
        if event == 'StartNeuesSpiel':
            window = gameName()
        elif event == 'StartMitwirkende':
            window = mitwirkendeWindow()
        elif event == 'MitwirkendeZurück':
            window = startWindow()
        elif event in (None, 'StartBeenden'):
            break
        elif event == 'NameBestätigen':
            if values['username'] == '':
                sg.popup('Bitte trage einen Namen ein!')
            else:
                window = newGame()
    print(values['username'])
    window.close()

if __name__ == '__main__':
    startGame()