"""
Inventory
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    # your code goes here
    for i in range(len(addedItems)):
        for key in inventory.keys():
            if addedItems[i] != key:
                inventory[addedItems[i]] = 1
            else:
                inventory[addedItems[i]] += 1
    return inventory


def addToInventory2(inventory, addedItems):
    for i in range(len(addedItems)):
        for key, val in inventory.items():
            if key == addedItems[i]:
                val += 1
            else:
                inventory.setdefault(addedItems[i], 1)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory2(inv, dragonLoot)
displayInventory(inv)
