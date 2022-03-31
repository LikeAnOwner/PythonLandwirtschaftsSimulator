import imp
from rich import print
from commands import getCommands
import json
from helper import *


name = ''
if not isGameNew():
    loadGame = input('Es wurde ein Spielstand gefunden. Möchtest du den Spielstand laden? (j/n)' + '\n> ')

    while loadGame != 'j' or loadGame != 'n':
        if loadGame == 'j':
            break
        elif loadGame == 'n':
            resetGameData()
            print('Bitte gib deinen Namen ein.')
            name = input('> ')
            break
        else:
            print('[red]Bitte gib eine gültige Antwort ein![/red]')
            loadGame = input('Es wurde ein Spielstand gefunden. Möchtest du den Spielstand laden? (j/n)' + '\n> ')
else:
    print('Bitte gib deinen Namen ein.')
    name = input('> ')
    resetGameData()

game_data = loadGameData()

def main():
    if name == 'Pant':
        print('[chartreuse4]      _\______[/chartreuse4]')
        print('[chartreuse4]      /        \========[/chartreuse4]')
        print('[chartreuse4] ____|__________\_____[/chartreuse4]')
        print('[chartreuse4]/ ___________________ \\ [/chartreuse4]')
        print('[chartreuse4]\/ _===============_ \/[/chartreuse4]')
        print('[chartreuse4]  "-===============-"[/chartreuse4]\n')
        print('\n[red]Sie sind mit Ihrem Panzer über den Hof gefahren und haben dabei alles zerstört...[/red]')
        print('\n[red]Game Over[/red]')
        exit()
    elif name == '':
        game_data['name'] = name
        print('\n[chartreuse4]Herzlich Willkommen ' + game_data['name'] + ' zum Python Farming Simulator![/chartreuse4]', ':tractor:')
        print('\nDu hast den alten Hof deines Großvaters geerbt. Leider sehen die Bilanzen gar nicht gut aus...')
        print('\nVerwende den Befehl \'hilfe\', um eine Auflistung aller aktuell zur Verfügung stehenden Befehle zu erhalten.\n')
    else:
        print('Willkommen zurück ' + game_data['name'] + '!')

    while True:
        eingabe = input('> ')
        getCommands(eingabe)

main()
