import random
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich import print
from helper import *
import time

def sendCommand(command):
    args = command.split()
    game_data = loadGameData()

    if args[0] == 'hilfe':
        hilfe()
    elif args[0] == 'felder':
        felder(game_data)
    elif args[0] == 'lockern':
        if len(args) != 2:
            print(f'Bitte verwende \'lockern feldId\', um das entsprechende Feld zu selektieren.')
            return
        try:
            int(args[1])
        except ValueError:
            print(f'[red]Bitte verwende als \'feldId\' eine Nummer.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        if int(args[1]) > len(game_data['fields']):
            print(f'[red]Das Feld mit der ID {args[1]} existiert nicht.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        lockern(game_data, args[1])
    elif args[0] == 'pflanzen':
        if len(args) != 2:
            print(f'Bitte verwende \'pflanzen feldId\', um das entsprechende Feld zu selektieren.')
            return
        try:
            int(args[1])
        except ValueError:
            print(f'[red]Bitte verwende als \'feldId\' eine Nummer.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        if int(args[1]) > len(game_data['fields']):
            print(f'[red]Das Feld mit der ID {args[1]} existiert nicht.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        pflanzen(game_data, args[1])
    elif args[0] == 'gießen':
        if len(args) != 2:
            print(f'Bitte verwende \'gießen feldId\', um das entsprechende Feld zu selektieren.')
            return
        try:
            int(args[1])
        except ValueError:
            print(f'[red]Bitte verwende als \'feldId\' eine Nummer.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        if int(args[1]) > len(game_data['fields']):
            print(f'[red]Das Feld mit der ID {args[1]} existiert nicht.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        gießen(game_data, args[1])
    elif args[0] == 'ernten':
        if len(args) != 2:
            print(f'Bitte verwende \'ernten feldId\', um das entsprechende Feld zu selektieren.')
            return
        try:
            int(args[1])
        except ValueError:
            print(f'[red]Bitte verwende als \'feldId\' eine Nummer.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        if int(args[1]) > len(game_data['fields']):
            print(f'[red]Das Feld mit der ID {args[1]} existiert nicht.[/red]\nDu kannst deine Felder mit dem Befehl \'felder\' anzeigen lassen.')
            return
        ernten(game_data, args[1])
    elif args[0] == 'verlassen':
        verlassen(game_data)
    else:
        print(f'Der Befehl \'{command}\' existiert nicht. Bitte verwende \'hilfe\', um eine Auflistung aller aktuell zur Verfügung stehenden Befehle zu erhalten.')
    saveGameData(game_data)

def hilfe():
    console = Console()
    table = Table(show_header=True, header_style="chartreuse4")
    table.add_column('Befehl')
    table.add_column('Beschreibung')
    table.add_row('hilfe', 'Zeigt eine Auflistung aller aktuell zur Verfügung stehenden Befehle.')
    table.add_row('felder', 'Zeigt eine Auflistung aller Felder an.')
    table.add_row('lockern feldId', 'Lockert das angegebene Feld auf.')
    table.add_row('pflanzen feldId', 'Pflanzt das angegebene Feld.')
    table.add_row('gießen feldId', 'Gießt das angegebene Feld.')
    table.add_row('ernten feldId', 'Erntet das angegebene Feld.')
    table.add_row('verlassen', 'Verlässt das Spiel.')

    console.print(table)

def felder(game_data):
    console = Console()
    table = Table(show_header=True, header_style="chartreuse4")
    table.add_column('Feld')
    table.add_column('Typ')
    table.add_column('Status')
    
    for feld in game_data['fields']:
        table.add_row(str(feld['id']), feld['type'], feld['status'])

    console.print(table)

def lockern(game_data, feldId):
    if game_data['fields'][int(feldId) - 1]['status'] != 'harvested':
        print('[red]Ein Feld muss geerntet sein um es lockern zu können.[/red]')
        print('Du kannst dir weitere Felder mit dem Befehl \'felder\' anzeigen lassen.')
        return

    with Progress() as progress:
        task3 = progress.add_task("[chartreuse4]Lockern...", total=random.randint(650, 1100))
        while not progress.finished:
            progress.update(task3, advance=1)
            time.sleep(0.02)

    game_data['fields'][int(feldId) - 1]['status'] = 'loosened'
    print('Das Feld ' + feldId + ' wurde gelockert.')

def pflanzen(game_data, feldId):
    if game_data['fields'][int(feldId) - 1]['status'] != 'loosened':
        print('[red]Ein Feld muss gelockert sein um es bepflanzen zu können.[/red]')
        print('Du kannst dir weitere Felder mit dem Befehl \'felder\' anzeigen lassen.')
        return

    with Progress() as progress:
        task3 = progress.add_task("[chartreuse4]Pflanzen...", total=random.randint(650, 1100))
        while not progress.finished:
            progress.update(task3, advance=1)
            time.sleep(0.02)

    game_data['fields'][int(feldId) - 1]['status'] = 'planted'
    print('Das Feld ' + feldId + ' wurde bepflanzt.')

def gießen(game_data, feldId):
    if game_data['fields'][int(feldId) - 1]['status'] != 'planted':
        print('[red]Ein Feld muss bepflanzt sein um es gießen zu können.[/red]')
        print('Du kannst dir weitere Felder mit dem Befehl \'felder\' anzeigen lassen.')
        return

    with Progress() as progress:
        task3 = progress.add_task("[chartreuse4]Gießen...", total=random.randint(650, 1100))
        while not progress.finished:
            progress.update(task3, advance=1)
            time.sleep(0.02)

    game_data['fields'][int(feldId) - 1]['status'] = 'doused'
    print('Das Feld ' + feldId + ' wurde gegossen.')

def ernten(game_data, feldId):    
    if game_data['fields'][int(feldId) - 1]['status'] != 'doused':
        print('[red]Ein Feld muss gegossen sein um es ernten zu können.[/red]')
        print('Du kannst dir weitere Felder mit dem Befehl \'felder\' anzeigen lassen.')
        return

    with Progress() as progress:
        task3 = progress.add_task("[chartreuse4]Ernten...", total=random.randint(650, 1100))
        while not progress.finished:
            progress.update(task3, advance=1)
            time.sleep(0.02)

    game_data['fields'][int(feldId) - 1]['status'] = 'harvested'
    print('Das Feld ' + feldId + ' wurde geerntet.')
    print('[chartreuse4]Ein neues Feld wurde zu deinen Feldern hinzugefügt.[/chartreuse4]')
    new_feld = {
        'id': len(game_data['fields']) + 1,
        'type': random.choice(['potato', 'wheat', 'corn', 'carrot', 'tomato', 'weed', 'asparagus', 'pumpkin']),
        'status': 'harvested'
    }
    game_data['fields'].append(new_feld)

def verlassen(game_data):
    saveGameData(game_data)
    clear()
    exit()
