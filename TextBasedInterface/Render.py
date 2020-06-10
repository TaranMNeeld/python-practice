import inspect
from HealthBar import render_bar


def render(player):
    player_class = inspect.getmembers(player)
    player_stats = [member[1] for member in player_class if member[0] == '__dict__'][0]['data']

    print(player_stats)
    render_bar(player.data['max_hp'], player.data['current_hp'])
