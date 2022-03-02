from rich.console import Console
from rich.table import Table

def showAufgaben():
    console = Console()

    table = Table(show_header=True, header_style='bold magenta')
    table.add_column('Befehl')
    table.add_column('Aufgabe')
    table.add_column('Kosten', justify='right')
    table.add_row('lockern', 'Erde der Felder lockern', '10 Energie')
    table.add_row('pflanzen', 'Felder bepflanzen', '20 Energie')
    table.add_row('gießen', 'Felder begießen', '30 Energie')
    table.add_row('ernten', 'Felder ernten', '40 Energie')

    console.print(table)
    print()