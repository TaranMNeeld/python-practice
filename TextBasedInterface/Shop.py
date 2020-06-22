from Item import Item

shop_items = {
    'torch': Item('torch', 'the flame glows bright', 5),
    'dagger': Item('dagger', 'it seems dull...', 10),
    'shield': Item('shield', 'sturdy enough to block an arrow', 10)
}


class Shop:
    def __init__(self, name, items=[item for item in shop_items]):
        self.name = name
        self.items = items

    def get_items(self):
        if len(self.items):
            return print(f'! The shop has the following items: {[item.name for item in self.items]}\n'
                         f'Enter [buy item_name]')

    def has_item(self, item):
        item_names = shop_items.keys()
        if item['name'] in item_names:
            return True
        else:
            return False

    def on_buy(self, item):
        return f'You bought {item["name"]} for {item["value"]} coins!'
