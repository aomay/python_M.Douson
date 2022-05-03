
inventory = ('меч',
            'щит',
            'кольчуга',
            'лечебное зелье')

chest = ('золото',
        'алмаз')

print ('\nтеперь в вашем инвентаре ', len(inventory), ' предметов:')
for items in inventory:
    print (items)

if 'лечебное зелье' in inventory:
    print('\nс зельем дела не так уж и плохи')

input ('press enter')

print ('\nвы нашли сундук в котором:')
for items in chest:
    print (items)

input('нажмите enter чтобы забрать предметы')
inventory += chest

print ('теперь в вашем инвентаре ', len(inventory), ' предметов:')
for items in inventory:
    print (items)

input ('press enter')
