from platform import system
from rich import print
from commands import *
from helper import *

if not isGameNew():
    clear()
    loadGame = input('\nEs wurde ein Spielstand gefunden. Soll der gespeicherte Spielstand geladen werden? (j/n)' + '\n\n> ')

    while loadGame != 'j' or loadGame != 'n':
        if loadGame == 'j':
            game_data = loadGameData()
            clear()
            print('\nWillkommen zurück ' + game_data['name'] + ', du kennst dich ja sicherlich noch auf deinem Hof aus.')
            print('Anderenfalls kannst du \'hilfe\' in die Konsole eingeben, um eine Liste aller verfügbaren Befehle zu erhalten.')
            break
        elif loadGame == 'n':
            resetGameData()
            break
        else:
            clear()
            print('\n[red]Bitte gib eine gültige Antwort ein![/red]')
            loadGame = input('Es wurde ein Spielstand gefunden. Möchtest du den Spielstand laden? (j/n)' + '\n\n> ')

if isGameNew():
    clear()
    print('\n[chartreuse4]Herzlich willkommen zum Python Farming Simulator von Ole und Jakob![/chartreuse4]')
    print('\nDu hast den alten Hof deines Großvaters geerbt, doch sehen die Bilanzen leider gar nicht gut aus.')
    print('Um den Hof nun wieder auf Vordermann zu bringen, müssen einige Aufgaben erledigt werden.\n')
    print('Bevor du richtig loslegen kannst, musst du nur noch die Erburkunde unterschrieben.')
    print('Bitte trag deinen Namen in die Konsole ein und bestätige mit der Eingabetaste.')

    name = input('\n> ')

    if name == 'Pant':
        clear()
        print('\n[chartreuse4]      _\______[/chartreuse4]')
        print('[chartreuse4]      /        \========[/chartreuse4]')
        print('[chartreuse4] ____|__________\_____[/chartreuse4]')
        print('[chartreuse4]/ ___________________ \\ [/chartreuse4]')
        print('[chartreuse4]\/ _===============_ \/[/chartreuse4]')
        print('[chartreuse4]  "-===============-"[/chartreuse4]\n')
        print('\nAnstatt die Urkunde zu unterschreiben sind Sie mit einem Panzer vom Typen Leopard 2 über den alten Hof Ihres Großvaters gefahren.')
        print('\nDabei haben Sie den gesamten Hof zunichtegemacht.')
        print('\n\n[red1]GAME OVER[/red1]\n')
        exit()
    
    clear()
    print('\nNachdem du nun das Rechtliche abgeschlossen hast, kannst du mit der Abarbeitung der Aufgaben loslegen.')
    print('Um eine Auflistung aller Befehle zu erhalten, trage \'hilfe\' in die Konsole ein.')

    game_data = loadGameData()
    game_data['name'] = name
    saveGameData(game_data)

def main():
    while True:
        eingabe = input('\n> ')
        clear()
        print('\n> ' + eingabe)
        sendCommand(eingabe)

main()
