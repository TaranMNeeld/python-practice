import inspect
import json
import os
from Render import render
from Player import Player
import PlayerData
from CreateAccount import create_account

running = True


def start():
    global running
    player = Player()
    player_class = inspect.getmembers(player)
    player_stats = [member[1] for member in player_class if member[0] == '__dict__'][0]['data']

    while running:
        print(player_stats)
        print('Type one of the following commands: save, load, create, exit')
        cmd = str(input())

        if player.data['name'] is None:
            if cmd == 'load':
                player = PlayerData.load()
            if cmd == 'create':
                create_account()
            if cmd == 'exit':
                running = False
        else:
            if cmd == 'save':
                PlayerData.save(player)
            render(player_stats)


if __name__ == '__main__':
    start()
