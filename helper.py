import json
import os

def isGameNew():
    with open('game_data.json', 'r') as json_file:
        game_data = json.load(json_file)

    with open('default_data.json', 'r') as json_file:
        default_data = json.load(json_file)

    if game_data == default_data:
        return True
    else:
        return False

def resetGameData():
    with open('default_data.json', 'r') as json_file:
        default_data = json.load(json_file)

    with open('game_data.json', 'w') as json_file:
        json.dump(default_data, json_file)

def loadGameData():
    with open('game_data.json', 'r') as json_file:
        game_data = json.load(json_file)

    return game_data

def saveGameData(game_data):
    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
