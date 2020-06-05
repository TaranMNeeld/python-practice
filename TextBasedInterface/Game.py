import inspect
import json
import os
from Render import render
from Player import Player


def start():
    # Working on importing player stats to pass into player
    # Just using default values for now
    player = Player()

    # Get all of the attributes from the Player class
    player_class = inspect.getmembers(player)

    # Set player_stats to only the attributes inside of the constructor, which reside in __dict__
    # '[0]' was added to the end because the stats object is inside of the list made with the list comprehension
    # I need the stats as an object so I can easily write it to a file and read it with stringify
    player_stats = [member[1] for member in player_class if member[0] == '__dict__'][0]['data']

    if player.data["name"] is None:
        print('Please Enter Your Name: ')
        name = str(input())
        # Check if name is already in use by checking to see if the file exists
        # if os.path.exists(file_path)
        player.data["name"] = name

    if os.stat(f'{player.data["name"]}.txt').st_size == 0:
        player_data = open(f'{player.data["name"]}.txt', 'w')
        player_data.write(json.dumps(player_stats))
        player_data.close()
    player_data = open(f'{player.data["name"]}.txt', 'r')
    file_content = player_data.read()
    data = json.loads(file_content)
    player_data.close()

    player = Player(data)

    render(player_stats)


if __name__ == '__main__':
    start()
