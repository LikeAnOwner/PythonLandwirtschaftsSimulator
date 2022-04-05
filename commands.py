from rich.console import Console
from rich.table import Table
import json

def sendCommand(command):
    args = command.split()

    if args[0] == 'hilfe':
        hilfe()
    elif args[0] == 'felder':
        felder()
    elif args[0] == 'lockern':
        if len(args) != 2:
            print(f'\nBitte verwende \'lockern feldId\', um das entsprechende Feld zu selektieren.\n')
            return
        lockern(args[1])
    elif args[0] == 'pflanzen':
        if len(args) != 2:
            print(f'\nBitte verwende \'pflanzen feldId\', um das entsprechende Feld zu selektieren.\n')
            return
        pflanzen(args[1])
    elif args[0] == 'gießen':
        if len(args) != 2:
            print(f'\nBitte verwende \'gießen feldId\', um das entsprechende Feld zu selektieren.\n')
            return
        gießen(args[1])
    elif args[0] == 'ernten':
        if len(args) != 2:
            print(f'\nBitte verwende \'ernten feldId\', um das entsprechende Feld zu selektieren.\n')
            return
        ernten(args[1])
    else:
        print(f'\nDer Befehl \'{command}\' existiert nicht. Bitte verwende \'hilfe\', um eine Auflistung aller aktuell zur Verfügung stehenden Befehle zu erhalten.\n')

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

    console.print(table)
    print()

def felder():
    with open('game_data.json', 'r') as json_file:
        game_data = json.load(json_file)

    console = Console()
    table = Table(show_header=True, header_style="chartreuse4")
    table.add_column('Feld')
    table.add_column('Typ')
    table.add_column('Status')
    
    for feld in game_data['fields']:
        table.add_row(str(feld['id']), feld['type'], feld['status'])

    console.print(table)
    print()

def lockern(feldId):
    with open('game_data.json', 'r') as json_file:
        game_data = json.load(json_file)
        # print(game_data['fields'][0])
        # harvested, loosened, planted, doused
    
    if game_data['fields'][int(feldId) - 1]['status'] != 'harvested':
        print('Ein Feld muss geerntet sein um es lockern zu können.')
        return

    game_data['fields'][int(feldId) - 1]['status'] = 'loosened'

    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file)

    print('Das Feld ' + feldId + ' wurde gelockert.')

def pflanzen(feldId):
    with open('game_data.json', 'r') as json_file:
        game_data = json.load(json_file)
        # print(game_data['fields'][0])
        # harvested, loosened, planted, doused
    
    if game_data['fields'][int(feldId) - 1]['status'] != 'loosened':
        print('Ein Feld muss gelockert sein um es bepflanzen zu können.')
        return

    game_data['fields'][int(feldId) - 1]['status'] = 'planted'

    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file)

    print('Das Feld ' + feldId + ' wurde bepflanzt.')

def gießen(feldId):
    with open('game_data.json', 'r') as json_file:
        game_data = json.load(json_file)
        # print(game_data['fields'][0])
        # harvested, loosened, planted, doused
    
    if game_data['fields'][int(feldId) - 1]['status'] != 'planted':
        print('Ein Feld muss bepflanzt sein um es gießen zu können.')
        return

    game_data['fields'][int(feldId) - 1]['status'] = 'doused'

    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file)

    print('Das Feld ' + feldId + ' wurde gegossen.')

def ernten(feldId):
    with open('game_data.json', 'r') as json_file:
        game_data = json.load(json_file)
        # print(game_data['fields'][0])
        # harvested, loosened, planted, doused
    
    if game_data['fields'][int(feldId) - 1]['status'] != 'doused':
        print('Ein Feld muss gegossen sein um es ernten zu können.')
        return

    game_data['fields'][int(feldId) - 1]['status'] = 'harvested'

    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file)

    print('Das Feld ' + feldId + ' wurde geerntet.')