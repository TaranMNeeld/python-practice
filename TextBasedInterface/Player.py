class Player:

    def __init__(self, data={'name': None, 'level': 1, 'max_hp': 100, 'current_hp': 100, 'base_dmg': 2}):
        self.data = data

    def restore_hp(self, amount):
        