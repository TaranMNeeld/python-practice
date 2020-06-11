from Render import render_bar
from Player import Player
from Enemy import Enemy

battling = True


def render_battle(player, enemy):
    global battling
    while battling:
        render_bar(player.data['max_hp'], player.data['current_hp'])
        render_bar(enemy.data['max_hp'], enemy.data['current_hp'])

        if player.data['current_hp'] <= 0 or enemy.data['current_hp'] <= 0:
            break

        print('Type one of the following commands: attack, flee, heal')
        cmd = str(input())
        if cmd == 'flee':
            battling = False
        if cmd == 'heal':
            player.restore_hp(1000)
        if cmd == 'attack':
            print(f'You hit {player.attack()}')
            print(f'{enemy.data["name"]} hit {enemy.attack()}')
            player.data['current_hp'] -= enemy.attack()
            enemy.data['current_hp'] -= player.attack()
        player.clamp_hp()

    battling = False
