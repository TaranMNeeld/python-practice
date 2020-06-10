from Render import render
from Player import Player
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
            player.clamp_hp()
            render(player)


if __name__ == '__main__':
    start()
