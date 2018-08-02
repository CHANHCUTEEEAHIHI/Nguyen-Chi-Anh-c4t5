inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strangeberry', 'lint']
print(inventory)

inventory['backpack'].remove('dagger')
print(inventory)

inventory['gold'] +=50
print(inventory)