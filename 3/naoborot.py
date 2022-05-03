text = input ('введите текст: ')

new_text = ''
k = 1

for i in text:
    lit = text [-k]
    new_text += lit
    k += 1

print (new_text)

input ('нажмите enter')
