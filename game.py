from rich import print
from commands import getCommands
from helper import *


if not isGameNew():
    loadGame = input('Es wurde ein Spielstand gefunden. Soll der gespeicherte Spielstand geladen werden? (j/n)' + '\n> ')

    while loadGame != 'j' or loadGame != 'n':
        if loadGame == 'j':
            game_data = loadGameData()
            print('\nWilkommen zurück ' + game_data['name'] + ', du kennst dich ja sicherlich noch auf deinem Hof aus.')
            print('Anderenfalls kannst du \'hilfe\' in die Konsole eingeben, um eine Liste aller verfügbaren Befehle zu erhalten.')
            break
        elif loadGame == 'n':
            resetGameData()
            break
        else:
            print('\n[red]Bitte gib eine gültige Antwort ein![/red]')
            loadGame = input('Es wurde ein Spielstand gefunden. Möchtest du den Spielstand laden? (j/n)' + '\n> ')

if isGameNew():
    print('\n[chartreuse4]Herzlich Willkommen zum Python Farming Simulator von Ole und Jakob![/chartreuse4]')
    print('\nDu hast den alten Hof deines Großvaters geerbt doch sehen die Bilanzen leider gar nicht gut aus.')
    print('Um den Hof nun wieder auf vordermann zu Bringen müssen einige Aufgaben erledigt werden.\n')
    print('Beovr du richtig loslegen kanns musst du nur noch die erburkunde unterschrieben.')
    print('Bitte trag deinen Namen in die Konsole ein und bestätige mit der Eingabetaste.')

    name = input('> ')

    if name == 'Pant':
        print('\n[chartreuse4]      _\______[/chartreuse4]')
        print('[chartreuse4]      /        \========[/chartreuse4]')
        print('[chartreuse4] ____|__________\_____[/chartreuse4]')
        print('[chartreuse4]/ ___________________ \\ [/chartreuse4]')
        print('[chartreuse4]\/ _===============_ \/[/chartreuse4]')
        print('[chartreuse4]  "-===============-"[/chartreuse4]\n')
        print('\nAnstatt die Uhrkunde zu unterschreiben sie sind mit einem Panzer vom Typen Leopard 2 über den alten Hof Ihres Großvaters gefahren.')
        print('\nDabei haben Sie den gesamten Hof zunichte gemacht und Ihr Großvater dreht sich im Grab um.')
        print('\n\n[red1]GAME OVER[/red1]\n')
        exit()
    
    print('\nNachdem du nun das Rechtliche Abgeschlossen hast kannst du mit der Abarbeitung der Aufgaben losleglen.')
    print('Um eine Auflistung aller aktuell zur Verfügung stehenden Befehle zu erhalten, trage \'hilfe\' in die Konsole ein.')

    game_data = loadGameData()
    game_data['name'] = name
    saveGameData(game_data)

def main():
    while True:
        eingabe = input('> ')
        sendCommand(eingabe)

main()
