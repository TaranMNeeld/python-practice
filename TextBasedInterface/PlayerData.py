import os
import inspect
import json
from Player import Player

loading = True


def save(player):
    player_class = inspect.getmembers(player)
    player_stats = [member[1] for member in player_class if member[0] == '__dict__'][0]['data']

    player_data = open(f'{player.data["name"]}.txt', 'w')
    player_data.write(json.dumps(player_stats))
    player_data.close()


def load():
    global loading
    while loading:
        print('Please enter your account username')
        name = str(input())
        if os.path.exists(f'{name}.txt'):
            player_data = open(f'{name}.txt', 'r')
            file_content = player_data.read()
            data = json.loads(file_content)
            player_data.close()
            loading = False
            return data
        else:
            print('That account does not exist, please try again.')
