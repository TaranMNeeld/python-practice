from HealthBar import render_bar


def render(player_data):
    render_bar(player_data['max_hp'], player_data['current_hp'])
