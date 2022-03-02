from rich.console import Console
from rich.table import Table

commands = ['hilfe', 'aufgaben']

def showHilfe():
    console = Console()

    table = Table(show_header=True, header_style="chartreuse4")
    table.add_column('Befehl')
    table.add_column('Beschreibung')
    table.add_row('hilfe', 'Zeigt eine Auflistung aller aktuell zur Verfügung stehenden Befehle.')
    table.add_row('aufgaben', 'Zeigt eine Auflistung aller zu erledigenden Aufgaben.')
    
    console.print(table)
    print()