from Render import render_bar


def render_battle(player, enemy):
    while player.data['current_hp'] > 0 or enemy.data['current_hp'] > 0:
        render_bar(player.data['max_hp'], player.data['current_hp'])
        render_bar(enemy.data['max_hp'], enemy.data['current_hp'])
