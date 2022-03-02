from rich import print
from aufgaben import *
from helper import *
import feld

startFeld = feld.feld()

def gameLoop():
    eingabe = input('> ')
    while eingabe not in commands:
        print(f'\nDer Befehl \'{eingabe}\' existiert nicht. Bitte verwende \'hilfe\', um eine Auflistung aller aktuell zur Verfügung stehenden Befehle zu erhalten.\n')
        eingabe = input('> ')
    
    if eingabe == 'hilfe':
        showHilfe()
    elif eingabe == 'aufgaben':
        showAufgaben()
    elif eingabe == 'lockern':
        startFeld.lockern
    elif eingabe == 'pflanzen':
        startFeld.pflanzen
    elif eingabe == 'gießen':
        startFeld.gießen
    elif eingabe == 'ernten':
        startFeld.ernten
    
    gameLoop()

print('\n[chartreuse4]Herzlich Willkommen zum Python Farming Simulator![/chartreuse4]', ':tractor:\n')
print('Du hast den alten Hof deines Großvaters geerbt. Leider sehen die Bilanzen gar nicht gut aus...\nUm die Rentabilität wieder herzustellen, müssen einige Aufgaben erledigt werden.')
print('\nVerwende den Befehl \'hilfe\', um eine Auflistung aller aktuell zur Verfügung stehenden Befehle zu erhalten.\n')

gameLoop()