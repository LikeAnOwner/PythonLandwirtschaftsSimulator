from rich import print
from commands import getCommands
import json

with open('default_data.json', 'r') as json_file:
    default_data = json.load(json_file)

with open('game_data.json', 'w') as json_file:
        json.dump(default_data, json_file)

with open('game_data.json', 'r') as json_file:
    game_data = json.load(json_file)

def main():
    print('Bitte gebe deinen Namen ein.')
    game_data['name'] = input('> ')

    if game_data['name'] == 'Pant':
        print('[chartreuse4]      _\______[/chartreuse4]')
        print('[chartreuse4]      /        \========[/chartreuse4]')
        print('[chartreuse4] ____|__________\_____[/chartreuse4]')
        print('[chartreuse4]/ ___________________ \\ [/chartreuse4]')
        print('[chartreuse4]\/ _===============_ \/[/chartreuse4]')
        print('[chartreuse4]  "-===============-"[/chartreuse4]')

    print('\n[chartreuse4]Herzlich Willkommen ' + game_data['name'] + ' zum Python Farming Simulator![/chartreuse4]', ':tractor:')
    print('\nDu hast den alten Hof deines Großvaters geerbt. Leider sehen die Bilanzen gar nicht gut aus...')
    print('\nVerwende den Befehl \'hilfe\', um eine Auflistung aller aktuell zur Verfügung stehenden Befehle zu erhalten.\n')

    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file)

    while True:
        eingabe = input('> ')
        getCommands(eingabe)

main()
