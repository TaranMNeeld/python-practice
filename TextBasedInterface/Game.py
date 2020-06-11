from Render import render
from Player import Player
from Enemy import Enemy
import Battle
import PlayerData
from CreateAccount import create_account

running = True
player = Player()


def start():
    global running

    while running:

        if player.data['name'] is None:
            print('Type one of the following commands: save, load, create, exit')
            cmd = str(input())
            if cmd == 'load':
                player.data = PlayerData.load()
                print(player.data)
            if cmd == 'create':
                create_account()
            if cmd == 'exit':
                running = False
        else:
            print('Type one of the following commands: heal, battle, save, exit')
            cmd = str(input())
            if cmd == 'save':
                PlayerData.save(player)
            if cmd == 'exit':
                running = False
            if cmd == 'heal':
                player.restore_hp(1000)
            if cmd == 'battle':
                skeleton = Enemy()
                skeleton.data['name'] = 'Skeleton'
                print(skeleton.data)
                Battle.render_battle(player, skeleton)
                del skeleton
            player.clamp_hp()
            render(player)

            if player.data['current_xp'] >= player.data['req_xp']:
                player.level_up()
                print('You leveled up!')


if __name__ == '__main__':
    start()
