import inspect
import json
import os
from Player import Player
import PlayerData


def create_account():
    player = Player()

    while player.data['name'] is None:
        print('Please Enter Your Name: ')
        name = str(input())

        if os.path.exists(f'{name}.txt'):
            print('This name is already in use. Please choose another name.')
        else:
            player.data["name"] = name
            PlayerData.save(player)