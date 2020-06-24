from Render import render
from Player import Player
from Enemy import Enemy
import Battle
import PlayerData
from CreateAccount import create_account
from Shop import Shop

running = True
player = Player()
shop = Shop()


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
            if player.data['current_room'] == 'shop':
                print('Type one of the following commands: inspect item_name, heal, battle, shop, save, exit')
            else:
                print('Type one of the following commands: heal, battle, shop, save, exit')
            cmd = str(input())

            if cmd == 'save':
                PlayerData.save(player)
            if cmd == 'exit':
                running = False
            if cmd == 'heal':
                player.restore_hp(1000)
            if cmd == 'battle':
                enemy = Enemy()
                enemy.data['current_hp'] = enemy.data['max_hp']
                enemy.data['name'] = 'Skeleton'
                print(enemy.data)
                Battle.render_battle(player, enemy)
                # del enemy
                # print('test')
            if cmd == 'shop':
                player.data['current_room'] = 'shop'
                shop.get_items()
            if 'inspect' in cmd:
                cmds = cmd.split()
                item = cmds[1]
                shop_items = [item.name for item in shop.items]
                if item in shop_items:
                    print(item)

            player.clamp_hp()
            render(player)

            if player.data['current_xp'] >= player.data['req_xp']:
                player.level_up()
                print('You leveled up!')


if __name__ == '__main__':
    start()
