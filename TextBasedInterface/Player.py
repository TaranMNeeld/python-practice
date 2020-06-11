

class Player:

    def __init__(self, data={'name': None, 'level': 1, 'max_hp': 100, 'current_hp': 100, 'base_dmg': 2}, dead=False):
        self.data = data
        self.dead = dead

    def restore_hp(self, amount):
        if self.data['current_hp'] == self.data['max_hp']:
            print('Your current health is already max.')
        if self.data['current_hp'] < self.data['max_hp']:
            self.data['current_hp'] += amount

    def clamp_hp(self):
        if self.data['current_hp'] > self.data['max_hp']:
            self.data['current_hp'] = self.data['max_hp']
        if self.data['current_hp'] < 0:
            self.data['current_hp'] = 0
            self.dead = True

    def attack(self):
        return self.data['base_dmg']
