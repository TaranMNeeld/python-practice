

class Player:

    def __init__(self, data={
                            'name': None,
                            'level': 1,
                            'max_hp': 100,
                            'current_hp': 100,
                            'base_dmg': 2,
                            'req_xp': 50,
                            'current_xp': 0,
                            'inventory': [],
                            'coins': 0
                            }):
        self.data = data

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

    def attack(self):
        return self.data['base_dmg']

    def level_up(self):
        self.data['level'] += 1
        self.data['current_xp'] -= self.data['req_xp']
        self.data['req_xp'] = self.data['level'] * 50
        self.data['max_hp'] = self.data['level'] * 100
        self.data['base_dmg'] += 1
