
inventory = ()

if not inventory:
    print('вы безоружны')

input('\npress enter\n')

inventory = ('меч',
            'щит',
            'кольчуга',
            'зелье')

print(inventory)

for item in inventory:
    print(item)

input('\npress enter')
