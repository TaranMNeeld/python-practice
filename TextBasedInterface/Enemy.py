class Enemy:

    def __init__(self, data={'name': None, 'level': 1, 'max_hp': 10, 'current_hp': 10, 'base_dmg': 1}):
        self.data = data

    def attack(self):
        return self.data['base_dmg']
